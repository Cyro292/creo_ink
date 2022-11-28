from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.CustomUser)
admin.site.register(models.Board)
admin.site.register(models.Participation)
admin.site.register(models.ConfigurationSet)
admin.site.register(models.Judgement)