from django.contrib import admin

# Register your models here.
from .models import ScreeningRule, ScreeningRuleAdmin

# Registering the models with the admin module
admin.site.register(ScreeningRule, ScreeningRuleAdmin)