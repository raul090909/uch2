from django.contrib import admin
from .models import *

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(Pos_order)
class PosOrderAdmin(admin.ModelAdmin):
    pass