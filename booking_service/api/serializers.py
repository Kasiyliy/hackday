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


class OrganizationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizations
        fields = ('id', 'name')

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'name' , 'parent')