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
