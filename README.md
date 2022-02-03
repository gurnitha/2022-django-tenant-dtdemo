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

#### 9. Create models: SweetType and Sweet

```py

# 1. Create SweetType model

# sweet_shared/models.py

# Django modules
from django.db import models

# Create your models here.


class SweetType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name 

# 3. Register to admin

# sweet_shared/admin.py

# Django modules
from django.contrib import admin

# Locals
from .models import SweetType

# Register your models here.


admin.site.register(SweetType)


# 3. Create Sweet model

# sweet_tenant/models.py

# Django modules
from django.db import models
from sweet_shared.models import SweetType

# Create your models here.


class Sweet(models.Model):
    sweet_type = models.ForeignKey(SweetType, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name 

# 3. Register to admin

# sweet_tenant/admin.py

# Django modules
from django.contrib import admin

# Locals
from .models import Sweet

# Register your models here.


admin.site.register(Sweet)

# New/modified files

        modified:   README.md
        modified:   sweet_shared/admin.py
        modified:   sweet_shared/models.py
        modified:   sweet_tenant/admin.py
        modified:   sweet_tenant/models.py
```

#### 10. Run migrations

```py


# Create migrations
(django-tenant) λ python manage.py makemigrations
Migrations for 'sweet_shared':
  sweet_shared\migrations\0001_initial.py
    - Create model SweetType
Migrations for 'sweet_tenant':
  sweet_tenant\migrations\0001_initial.py
    - Create model Sweet

# Apply migration
(django-tenant) λ python manage.py migrate
[standard:public] === Starting migration
[standard:public] Operations to perform:
[standard:public]   Apply all migrations: admin, auth, client, contenttypes, sessions, sweet_shared, sweet_tenant
[standard:public] Running migrations:
[standard:public]   Applying sweet_shared.0001_initial...
[standard:public]  OK
[standard:public]   Applying sweet_tenant.0001_initial...
[standard:public]  OK
[1/1 (100%) standard:demo] === Starting migration
[1/1 (100%) standard:demo] Operations to perform:
[1/1 (100%) standard:demo]   Apply all migrations: admin, auth, client, contenttypes, sessions, sweet_shared, sweet_tenant
[1/1 (100%) standard:demo] Running migrations:
[1/1 (100%) standard:demo]   Applying sweet_shared.0001_initial...
[1/1 (100%) standard:demo]  OK
[1/1 (100%) standard:demo]   Applying sweet_tenant.0001_initial...
[1/1 (100%) standard:demo]  OK

# New/modified files

        modified:   README.md
        new file:   sweet_shared/migrations/0001_initial.py
        new file:   sweet_tenant/migrations/0001_initial.py
```

#### 11. Create superuser for public and superuser for demo

```py

# Create superuser for public
(django-tenant) λ python manage.py createsuperuser
Username (leave blank to use 'hp'): admin
Email address:
Password:
Password (again):
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

# Create superuser for demo
(django-tenant) λ python manage.py create_tenant_superuser
Enter Tenant Schema ('?' to list schemas): ?
demo - demo.localhost
Enter Tenant Schema ('?' to list schemas): demo
Username (leave blank to use 'hp'): demoadmin
Email address:
Password:
Password (again):
The password is too similar to the username.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

# New/modified files

        modified:   README.md
```