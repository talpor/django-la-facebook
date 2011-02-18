=====
Usage
=====

Get ``django-la-facebook`` into your python path::

    pip install django-la-facebook
    
Add ``la_facebook`` to your INSTALLED_APPS in settings.py::

    INSTALLED_APPS = (
        ...
        'la_facebook',
        ...
        )
    
Add ``la_facebook`` to your root urlconf (urls.py)::

    urlpatterns = patterns('',
        ...,
        url(r"^la_facebook/", include("la_facebook.urls")),
        ...,        
    )

Settings
--------

In order to authenticate your site's users with Facebook, you need a unique
identifier for Facebook to associate your site with.  Facebook considers your
site an "app" and so you must acquire an ``FACEBOOK_APP_ID`` and 
``FACEBOOK_APP_SECRET`` from the
`Facebook Developer app <http://www.facebook.com/developers>`_.

See the documentation for :doc:`settings` about how to enter these values in your 
Django settings file.

Views
-----

TODO

Templates
---------

TODO

Template Tags
-------------

TODO

