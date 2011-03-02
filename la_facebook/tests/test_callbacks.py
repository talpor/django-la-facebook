import datetime
from django.test import TestCase
try:
    from django.test.client import RequestFactory
except ImportError:
    raise ImportError("callback tests require Django > 1.3 for RequestFactory")

from django.contrib.auth.models import User

from la_facebook.access import OAuthAccess
from la_facebook.callbacks.base import BaseFacebookCallback
# from la_facebook.la_fb_logging import logger
from la_facebook.models import UserAssociation

factory = RequestFactory()

class BaseCallbackTests(TestCase):

    urls = 'la_facebook.tests.urls'

    def setUp(self):
        # logger.debug("callback test case setup")
        self.request = factory.get('/callback',data={'next':'dummy'})
        test_user = User()
        test_user.username = 'test'
        test_user.save()
        self.request.user = test_user
        assoc = UserAssociation()
        assoc.user = test_user
        assoc.token = 'facebooktokenstring'
        assoc.expires = datetime.datetime.now() + datetime.timedelta(1)
        assoc.save()
        self.token = assoc.token
        self.access = OAuthAccess()

    def test_call(self):
        basecallback = BaseFacebookCallback()
        ret = basecallback(self.request, self.access, self.token)
        self.assertEquals(ret.status_code, 302)
        # logger.debug(str(ret._headers['location'][1]))
        self.assertEquals(ret._headers['location'][1], '/dummy' )

    def test_redirect_url(self):
        callback = BaseFacebookCallback()
        resp = callback.redirect_url(self.request)
        self.assertEquals(resp,'dummy')

    def test_identifier_from_data(self):
        callback = BaseFacebookCallback()
        data = {'name':'test name','id':'testid'}
        resp = callback.identifier_from_data(data)
        self.assertEquals(resp,'test-name-testid')

 # Boilerplated, only tests that # of args not changed in regression:

    def test_fetch_user_data(self):
        callback = BaseFacebookCallback()
        self.assertRaises(NotImplementedError,callback.fetch_user_data,
                'arg','arg','arg')

    def test_lookup_user(self):
        callback = BaseFacebookCallback()
        self.assertRaises(NotImplementedError,callback.lookup_user,
                'arg','arg','arg')

    def test_handle_no_user(self):
        callback = BaseFacebookCallback()
        self.assertRaises(NotImplementedError,callback.handle_no_user,
                'arg','arg','arg','arg')

    def test_handle_unauthenticated_user(self):
        callback = BaseFacebookCallback()
        self.assertRaises(NotImplementedError,callback.handle_unauthenticated_user,
                'arg','arg','arg','arg','arg')
