from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import TestCase

from la_facebook.models import UserAssociation

class BasicViews(TestCase):
    
    
    def test_la_facebook_login(self):
        """ Django test client does not let us http off
                our server. So we just look for the right
                pointers to the facebook site
        """
        
        self.url = reverse('la_facebook_login')        
        
        # we have 302?
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        
        # Now check on the location header passed to the browser
        location = response._headers['location'][1]
        
        # Are we going to the right location?
        self.assertTrue("https://graph.facebook.com/oauth/authorize" in location)
        
        # Is the facebook APP ID in the location header?
        app_id = settings.FACEBOOK_ACCESS_SETTINGS['FACEBOOK_APP_ID']
        self.assertTrue(location.endswith(app_id))