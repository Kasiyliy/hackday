from rest_framework import generics
from django.apps import apps
from .serializers import *

Organizations = apps.get_model('system', 'Organizations')
Categories = apps.get_model('system', 'Categories')
ServiceTypes = apps.get_model('system', 'ServiceTypes')
WeekDays = apps.get_model('system', 'WeekDays')
TimeOffs = apps.get_model('system', 'TimeOffs')
Services = apps.get_model('system', 'Services')
ServiceNodes = apps.get_model('system', 'ServiceNodes')
Schedules = apps.get_model('system', 'Schedules')

class OrganizationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organizations.objects.all()
    model = Organizations
    serializer_class = OrganizationsSerializer

class OrganizationsList(generics.ListCreateAPIView):
    queryset = Organizations.objects.all()
    model = Organizations
    serializer_class = OrganizationsSerializer