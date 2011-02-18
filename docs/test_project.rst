========================
Running The Test Project
========================

#. Make sure you have Django 1.2 or greater and oauth2 at 1.5.163 or greater installed
#. Change directory to la_facebook/test_project
#. python manage.py syncdb
#. python manage.py runserver localhost:8000
#. Open a browser and point to that URL
#. Manually do the tests 

Logging
-------

By default the project will print debug level logging info both to stdout and 
to a log file located at /tmp/la_facebook.log.
