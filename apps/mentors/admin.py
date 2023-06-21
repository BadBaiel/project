from django.contrib import admin
from . import models


admin.site.register(models.Mentor)
admin.site.register(models.Employment)
admin.site.register(models.Skills)

