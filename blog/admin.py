from django.contrib import admin
from .models import Eco


class EcoAdmin(admin.ModelAdmin):
    list_display = ('ecouser','ecocount','ecotime')

admin.site.register(Eco, EcoAdmin)