# Django-easyregistration

Simple Django app to manage frontend users login/logout and registration process, build with class based views and Twitter Bootstrap.

## Demo

<img src="/docs/demo.gif"/>

## Updated

* 0.2 (December 26th, 2020): Django 3.0 compatibility check. 
* 0.1beta (December 31th, 2013): Spanish localization added.

## Quick start

1. Install it with pip in your env::

```bash
pip install django-easyregistration
```

2. Add `registration` to your `INSTALLED_APPS` settings:

```python
INSTALLED_APPS = (
    # ...
    'registration',
)
```

3. Include the registration URLconf in your project `urls.py`:

```python
urlpatterns = [
    .# .. 
	path('accounts/', include('registration.urls')),
]
```

4. Configure your preferred URLS in `registration/config.py` file.

5. Start the development server and visit http://127.0.0.1:8000/accounts/login/ or create an account at http://127.0.0.1:8000/accounts/register/.