from django.contrib import admin
from .models import Depositos

# Register your models here.

class DepositoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Depositos, DepositoAdmin)