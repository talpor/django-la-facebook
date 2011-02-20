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
        
        url = reverse('la_facebook_login')        
        
        # we have 302?
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)
        
        # Now check on the location header passed to the browser
        location = response._headers['location'][1]
        
        # Are we going to the right location?
        self.assertTrue("https://graph.facebook.com/oauth/authorize" in location)
        
        # Is the facebook APP ID in the location header?
        app_id = settings.FACEBOOK_ACCESS_SETTINGS['FACEBOOK_APP_ID']
        self.assertTrue(location.endswith(app_id))
        
    def test_facebook_callback(self):
        """ This only supports failure.
            TODO: make it cover success
        
        """
        url = reverse('la_facebook_callback')
        response = self.client.get(url)
        self.assertContains(response, "OAuth Error: token_mismatch")