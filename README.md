# BUILDING DJANGO-TENANTS SWEETSHOP


This is my exercise BUILDING MULTI TENANT SWEETSHOP based on the tutorials made by  Tom's Python and Django on Youtube
Tutorials on Youtube: https://www.youtube.com/channel/UCUKoRhPhS0INxh6RC1xN_TQ


#### 1. Create django project and app


```bash
# Create project
(django-tenant) λ django-admin startproject dtdemo

# Create app
(django-tenant) λ django-admin startapp client

# New/modified files

        new file:   .gitignore
        new file:   README.md
        new file:   client/__init__.py
        new file:   client/admin.py
        new file:   client/apps.py
        new file:   client/migrations/__init__.py
        new file:   client/models.py
        new file:   client/tests.py
        new file:   client/views.py
        new file:   dtdemo/__init__.py
        new file:   dtdemo/asgi.py
        new file:   dtdemo/settings.py
        new file:   dtdemo/urls.py
        new file:   dtdemo/wsgi.py
        new file:   manage.py
````

#### 2. Create Client and Domain models

```py

# shop/models.

# Django modules
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

# Create your models here.


# MODEL: Shop as client
class Client(TenantMixin):

	name = models.CharField(max_length=100)

	# Default true, schema will be authomatically 
	# created and synced when it is save
	auto_create_schema = True

	def __str__(self):
		return self.name 


# MODEL: Domain
class Domain(DomainMixin):
	pass 

# New/modified files

        modified:   README.md
        modified:   client/models.py
```

#### 3. Set database and db router

```py

# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'django_tenant_guide_2022',
        'USERNAME': 'postgres',
        'PASSWORD': 'ing',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}


# DATABASE ROUTER
DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

# New/modified files

        modified:   README.md
        modified:   dtdemo/settings.py
```

#### 4. Adding TenantMainMiddleware

```py

# Add middleware
MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware', # new TenantMainMiddleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# New/modified files

        modified:   README.md
        modified:   dtdemo/settings.py
```

#### 5. Split the settings.py file

```py
SHARED_APPS = [
    'django_tenants', # new

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Locals
    'client',
]


TENANT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Locals
    'client',
]


INSTALLED_APPS = list(SHARED_APPS) + [
    app for app in TENANT_APPS if app not in SHARED_APPS
]

# New/modified files

        modified:   README.md
        modified:   dtdemo/settings.py
```

#### 6. Configure TENANT_MODEL and TENANT_DOMAIN_MODEL

```py
# Define on settings.py which model is your tenant model. 
# Assuming you created Client inside an app named client, 
# your TENANT_MODEL should look like this:

TENANT_MODEL        = "client.Client" # app.Model
TENANT_DOMAIN_MODEL = "client.Domain" # app.Model

# New/modified files

        modified:   README.md
        modified:   dtdemo/settings.py
```

#### 7. Create new db schema called 'demo'

```py
# Create db schema 'demo'

E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide\dtdemo (master)
(django-tenant) λ python manage.py create_tenant
schema name: demo
name: demo
[1/1 (100%) standard:demo] === Starting migration
[1/1 (100%) standard:demo] Operations to perform:
[1/1 (100%) standard:demo]   Apply all migrations: admin, auth, client, contenttypes, sessions
...
[1/1 (100%) standard:demo]   Applying sessions.0001_initial...
[1/1 (100%) standard:demo]  OK
domain: demo.localhost
is primary (leave blank to use 'True'):

# New/modified files

        modified:   README.md
        new file:   client/migrations/0001_initial.py
```

#### 8. Create sweet_shared and sweet_tenant apps

```py

# Create apps

(django-tenant) λ python manage.py startapp sweet_shared
(django-tenant) λ python manage.py startapp sweet_tenant

# Install the a pps

SHARED_APPS = [

    'django_tenants', # new

    # Locals
    'client',   

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'sweet_shared',
]


TENANT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Locals
    'client',
    'sweet_tenant',
]

# New/modified files

        modified:   README.md
        modified:   dtdemo/settings.py
        new file:   sweet_shared/__init__.py
        new file:   sweet_shared/admin.py
        new file:   sweet_shared/apps.py
        new file:   sweet_shared/migrations/__init__.py
        new file:   sweet_shared/models.py
        new file:   sweet_shared/tests.py
        new file:   sweet_shared/views.py
        new file:   sweet_tenant/__init__.py
        new file:   sweet_tenant/admin.py
        new file:   sweet_tenant/apps.py
        new file:   sweet_tenant/migrations/__init__.py
        new file:   sweet_tenant/models.py
        new file:   sweet_tenant/tests.py
        new file:   sweet_tenant/views.py
```