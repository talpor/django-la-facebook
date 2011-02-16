from django.conf.urls.defaults import *
from django.contrib import admin 
admin.autodiscover()
urlpatterns = patterns('',
    url(r'^', include('test_project.connect.urls')),
    url(r"^la_facebook/", include("la_facebook.urls")),
    url(r'^admin/(.*)', admin.site.root),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'next_page':'/'}, name="logout")
)
