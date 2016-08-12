=====
GP Auth
=====

GP Auth is a simple application Django to manage the registration 
of users in a customized manner system.
To customize the user account just inherit the GP Auth.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "gp_auth" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'gpauth',
    ]

2. Include GP Auth User Model your settings.py project like this ::

    AUTH_USER_MODEL = 'gpauth.User'

3. Run `python manage.py migrate` to create the gp_auth models.

4. Run `python manage.py createsuperuser` to create a Super User.

5. Start the development server and visit http://127.0.0.1:8000/gpauth/
   to create a users (you'll need the Admin app enabled).
