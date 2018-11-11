from django.contrib import admin
from .models import *
# Register your models here.

class OrganizationAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_per_page = 10


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name','parent')
    list_display = ('name','parent')
    list_per_page = 10


class ServiceTypeAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_per_page = 10


class WeekDayAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
    list_per_page = 10


class TimeOffAdmin(admin.ModelAdmin):
    list_per_page = 10


class ServiceAdmin(admin.ModelAdmin):
    list_per_page = 10

class ServiceNodeAdmin(admin.ModelAdmin):
    list_display = ('service', 'service_type' ,'name' ,'servicer' , 'price')
    list_per_page = 10


class ScheduleAdmin(admin.ModelAdmin):
    list_filter = ('service_node',)
    list_display = ('begin_time', 'end_time', 'exact_day', 'client', 'phone_number' , 'service_node')
    list_per_page = 10


class RoleAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', )
    list_per_page = 10


class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_per_page = 10

class UserScheduleAdmin(admin.ModelAdmin):
    list_display = ('user', 'time_off')
    list_per_page = 10

admin.site.register(Organizations, OrganizationAdmin)
admin.site.register(Categories, CategoryAdmin)
admin.site.register(ServiceTypes, ServiceTypeAdmin)
admin.site.register(WeekDays, WeekDayAdmin)
admin.site.register(TimeOffs, TimeOffAdmin)
admin.site.register(Services, ServiceAdmin)
admin.site.register(ServiceNodes, ServiceNodeAdmin)
admin.site.register(Schedules, ScheduleAdmin)
admin.site.register(Roles, RoleAdmin)
admin.site.register(UserRoles, UserRoleAdmin)
admin.site.register(UserSchedules, UserScheduleAdmin)