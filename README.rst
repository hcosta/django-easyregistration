Django-easyregistration
=======================

** The easy way to manage frontend users auth and registration in `Django <http://www.djangoproject.com>`**

Django-easyregistration is a simple Django app to manage frontend users login/logout and registration process, build with class based views and Twitter Bootstrap.

Requirements
-----------

* Django 1.5/1.6

Releases
-----------

* Django-easyregistration 0.1beta (December 31th, 2013): Unstable

Quick start
-----------

1. Copy 'registration' directory inside your project root or install it::

      python setup.py install

2. Add "registration" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'registration',
      )

3. Include the registration URLconf in your project urls.py like this::

      url(r'^accounts/', include('registration.urls')),

4. Configure manually your preferred URLS in 'registration/config.py' file.

5. Start the development server and visit http://127.0.0.1:8000/accounts/login/ or  create an account at http://127.0.0.1:8000/login/accounts/register/.