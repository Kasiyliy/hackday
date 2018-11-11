from rest_framework import generics
from .serializers import *
from django.apps import apps
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import FileUploadParser
from datetime import datetime

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

class ImageUploadParser(FileUploadParser):
	media_type = 'image/*'

class MyViewSet(ViewSet):
    parser_class = (ImageUploadParser,)
    renderer_classes = (JSONRenderer,)

    def book(self, request, format=None):
        if (request.method == 'POST'):
            arr = {'begin_time' , 'end_time', 'exact_day' ,'client' ,'phone_number', 'service_node'}
            for element in arr:
                if (element not in request.data):
                    return Response({"message": "One of the required fields is empty!"})

            schedule = Schedules()
            schedule.begin_time = datetime.now().time()

            try:
                try:
                    schedule.begin_time = datetime.strptime(str(request.data['begin_time']), '%H:%M:%S').time()
                except Exception as e:
                    return Response({"message": str(e) })

                try:
                    schedule.end_time = datetime.strptime(request.data['end_time'], '%H:%M:%S').time()
                except Exception as e:
                    return Response({"message": str(e)})

                if schedule.begin_time > schedule.end_time:
                    return Response({"message": "Invalid begin time and end time"})
                try:
                    schedule.exact_day = datetime.strptime(request.data['exact_day'], "%Y-%m-%d").date()
                except:
                    return Response({"message": "Invalid exact_day "})

                try:
                    schedule.client = request.data['client']
                except:
                    return Response({"message": "Invalid client!"})

                try:
                    schedule.phone_number = int(request.data['phone_number'])
                except:
                    return Response({"message": "Invalid phone_number!"})

                try:
                    schedule.service_node = ServiceNodes.objects.get(pk=int(request.data['service_node']))
                except Exception as e:
                    return Response({"message": str(e)})
                schedule.save()
            except:
                return Response({"message": "Invalid format!"})
            return Response({"message": "Saved!" , 'link': 'https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=http://127.0.0.1:8000/api/schedules/' + str(schedule.id)})



class OrganizationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organizations.objects.all()
    model = Organizations
    serializer_class = OrganizationsSerializer

class OrganizationsList(generics.ListCreateAPIView):
    queryset = Organizations.objects.all()
    model = Organizations
    serializer_class = OrganizationsSerializer

class CategoriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    model = Categories
    serializer_class = CategoriesSerializer

class CategoriesList(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    model = Categories
    serializer_class = CategoriesSerializer

class ServiceTypesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceTypes.objects.all()
    model = ServiceTypes
    serializer_class = ServiceTypesSerializer

class ServiceTypesList(generics.ListCreateAPIView):
    queryset = ServiceTypes.objects.all()
    model = ServiceTypes
    serializer_class = ServiceTypesSerializer

class ServicesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Services.objects.all()
    model = Services
    serializer_class = ServicesSerializer

class ServicesList(generics.ListCreateAPIView):
    queryset = Services.objects.all()
    model = Services
    serializer_class = ServicesSerializer

class ServiceNodesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceNodes.objects.all()
    model = ServiceNodes
    serializer_class = ServiceNodesSerializer

class ServiceNodesList(generics.ListCreateAPIView):
    queryset = ServiceNodes.objects.all()
    model = ServiceNodes
    serializer_class = ServiceNodesSerializer

class TimeOffsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeOffs.objects.all()
    model = TimeOffs
    serializer_class = TimeOffsSerializer

class TimeOffsList(generics.ListCreateAPIView):
    queryset = TimeOffs.objects.all()
    model = TimeOffs
    serializer_class = TimeOffsSerializer

class SchedulesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedules.objects.all()
    model = Schedules
    serializer_class = SchedulesSerializer

class SchedulesList(generics.ListCreateAPIView):
    queryset = Schedules.objects.all()
    model = Schedules
    serializer_class = SchedulesSerializer

class WeekDaysDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeekDays.objects.all()
    model = WeekDays
    serializer_class = WeekDaysSerializer

class WeekDaysList(generics.ListCreateAPIView):
    queryset = WeekDays.objects.all()
    model = WeekDays
    serializer_class = WeekDaysSerializer

class RolesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roles.objects.all()
    model = Roles
    serializer_class = RolesSerializer


class RolesList(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    model = Roles
    serializer_class = RolesSerializer

class UserRolesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserRoles.objects.all()
    model = UserRoles
    serializer_class = UserRolesSerializer

class UserRolesList(generics.ListCreateAPIView):
    queryset = UserRoles.objects.all()
    model = UserRoles
    serializer_class = UserRolesSerializer


class UserSchedulesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserRoles.objects.all()
    model = UserRoles
    serializer_class = UserRolesSerializer

class UserSchedulesList(generics.ListCreateAPIView):
    queryset = UserSchedules.objects.all()
    model = UserSchedules
    serializer_class = UserSchedulesSerializer
