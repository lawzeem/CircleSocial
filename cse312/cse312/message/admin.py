from django.contrib import admin
from . import models

admin.site.register(models.Thread)
admin.site.register(models.ChatMessage)
