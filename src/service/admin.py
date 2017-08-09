from django.contrib import admin
from .models import Service, Item, Order

# Register your models here.

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'time_step', 'edited')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'is_active', 'created')
    list_filter = ('location', 'is_active')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user_info', 'item', 'time_start', 'time_end')
    def get_user_info(self, obj):
        return '{0}, {1}'.format(obj.get_full_name(), obj.group_number)
