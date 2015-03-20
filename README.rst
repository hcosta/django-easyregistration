Django-easyregistration
=======================

**The easy way to manage frontend users auth and registration in Django**

Django-easyregistration is a simple Django app to manage frontend users login/logout and registration process, build with class based views and Twitter Bootstrap.

Screenshots
-----------
.. image:: http://blog.hcosta.info/portfolio/2013-12-django-easyregistration/screen1.png
   :align: center

.. image:: http://blog.hcosta.info/portfolio/2013-12-django-easyregistration/screen2.png
   :align: center

Requirements
-----------

* Django 1.5/1.6

Changes
-----------

* Django-easyregistration 0.1beta (December 31th, 2013): Spanish localization added.

Quick start
-----------

1. Install it with pip in your env::

    $ pip install django-easyregistration

2. Add "registration" to your INSTALLED_APPS setting like this::

.. code-block:: python

        INSTALLED_APPS = (
            ...
            'registration',
        )

3. Include the registration URLconf in your project urls.py like this::

.. code-block:: python

        url(r'^accounts/', include('registration.urls')),

4. Configure manually your preferred URLS in 'registration/config.py' file.

5. Start the development server and visit http://127.0.0.1:8000/accounts/login/ or create an account at http://127.0.0.1:8000/accounts/register/.
