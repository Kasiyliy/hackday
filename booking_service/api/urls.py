from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from rest_framework.authtoken import views as rest_framework_views
urlpatterns = [

    url(r'organizations/(?P<pk>[0-9]+)$', OrganizationsDetail.as_view(), name="organizations-detail"),
    url('organizations', OrganizationsList.as_view(), name="organizations-list"),

    url(r'categories/(?P<pk>[0-9]+)$', CategoriesDetail.as_view(), name="categories-detail"),
    url('categories', CategoriesList.as_view(), name="caregories-list"),

    url(r'service-types/(?P<pk>[0-9]+)$', ServiceTypesDetail.as_view(), name="service-types-detail"),
    url('service-types', ServiceTypesList.as_view(), name="service-types-list"),

    url(r'services/(?P<pk>[0-9]+)$', ServicesDetail.as_view(), name="services-detail"),
    url('services', ServicesList.as_view(), name="services-list"),

    url(r'service-nodes/(?P<pk>[0-9]+)$', ServiceNodesDetail.as_view(), name="service-nodes-detail"),
    url('service-nodes', ServiceNodesList.as_view(), name="service-nodes-list"),

    url(r'time-offs/(?P<pk>[0-9]+)$', TimeOffsDetail.as_view(), name="time-offs-detail"),
    url('time-offs', TimeOffsList.as_view(), name="time-offs-list"),

    url(r'schedules/(?P<pk>[0-9]+)$', SchedulesDetail.as_view(), name="schedules-detail"),
    url('schedules', SchedulesList.as_view(), name="schedules-list"),

    url(r'week-days/(?P<pk>[0-9]+)$', WeekDaysDetail.as_view(), name="week-days-detail"),
    url('week-days', WeekDaysList.as_view(), name="week-days-list"),

    url(r'roles/(?P<pk>[0-9]+)$', RolesDetail.as_view(), name="roles-detail"),
    url('roles', RolesList.as_view(), name="roles-list"),

    url(r'user-roles/(?P<pk>[0-9]+)$', UserRolesDetail.as_view(), name="user-roles-detail"),
    url('user-roles', UserRolesList.as_view(), name="user-roles-list"),

    url(r'user-schedules/(?P<pk>[0-9]+)$', UserSchedulesDetail.as_view(), name="user-schedules-detail"),
    url('user-schedules', UserSchedulesList.as_view(), name="user-schedules-list"),

    url(r'book/$', MyViewSet.as_view({'post' : 'book'}), name='book'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
