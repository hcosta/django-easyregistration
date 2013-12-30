=====
Registration
=====

Registration is a simple Django app to manage frontend users login/logout  
and registration process, build with Twitter Bootstrap and ready for testing.

Quick start
-----------

1. Add "registration" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'registration',
      )

2. Include the registration URLconf in your project urls.py like this::

      url(r'^accounts/', include('registration.urls')),

3. Configure manually your preferred URLS in 'registration/config.py' file.

4. Start the development server and visit http://127.0.0.1:8000/accounts/login/ 
or  create an account at http://127.0.0.1:8000/login/accounts/register/.