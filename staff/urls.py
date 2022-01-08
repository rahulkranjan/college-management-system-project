from django.urls import path
from staff.views import *


urlpatterns = [

    path('add-staff/', CreateStaff.as_view()),
    path('designation/', DesignationList.as_view()),
    path('designation/<pk>/', DesignationDetail.as_view()),
    path('staff-profile/', StaffProfileList.as_view()),
    path('staff-profile/<pk>/', StaffProfileDetail.as_view()),
    
]
