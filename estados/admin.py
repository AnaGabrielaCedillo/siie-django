from django.contrib import admin

# Register your models here.
from estados.models import Estado, Pais

admin.site.register(Estado)
admin.site.register(Pais)
