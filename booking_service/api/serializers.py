from rest_framework import serializers
from django.apps import apps

Organizations = apps.get_model('system', 'Organizations')
Categories = apps.get_model('system', 'Categories')
ServiceTypes = apps.get_model('system', 'ServiceTypes')
WeekDays = apps.get_model('system', 'WeekDays')
TimeOffs = apps.get_model('system', 'TimeOffs')
Services = apps.get_model('system', 'Services')
ServiceNodes = apps.get_model('system', 'ServiceNodes')
Schedules = apps.get_model('system', 'Schedules')
Roles = apps.get_model('system', 'Roles')
UserRoles = apps.get_model('system', 'UserRoles')
UserSchedules = apps.get_model('system', 'UserSchedules')


class OrganizationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizations
        fields = ('id', 'name')

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'name' , 'parent')

class ServiceTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceTypes
        fields = ('id', 'name')

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ('id', 'category', 'organization')

class ServiceNodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceNodes
        fields = ('id', 'service', 'service_type', 'name', 'servicer','price')

class TimeOffsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeOffs
        fields = ('id', 'week_day', 'begin_time', 'end_time', 'exact_day')

class SchedulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules
        fields = ('id', 'begin_time', 'end_time', 'exact_day', 'client', 'phone_number', 'service_node')

class WeekDaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekDays
        fields = ('id', 'name', 'order_number')

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ('id', 'name')

class UserRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoles
        fields = ('id', 'user', 'role')

class UserSchedulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSchedules
        fields = ('id', 'user', 'time_off')
