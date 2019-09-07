from django.contrib import admin
from . import models

admin.site.register(models.Friend)
admin.site.register(models.Belonging)
admin.site.register(models.Borrowed)
