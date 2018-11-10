from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from rest_framework.authtoken import views as rest_framework_views
urlpatterns = [

    url(r'organizations/(?P<pk>[0-9]+)$', OrganizationsDetail.as_view(), name="organizations-detail"),
    url('organizations', OrganizationsList.as_view(), name="organizations-list"),

]

urlpatterns = format_suffix_patterns(urlpatterns)