from django.urls import path
from student.views import *


urlpatterns = [

    path('student-profile/', StudentProfileList.as_view()),
    path('student-profile/<pk>/', StudentProfileDetail.as_view()),
    path('sem-wise-student/<pk>/', SemesterWiseStudentDetail.as_view()),
    path('sem-wise-student/', SemesterWiseStudentList.as_view()),
    path('certificate/', CertificateList.as_view()),
    path('certificate/<pk>/', CertificateDetail.as_view()),
    path('student-admission/', StudentAdmission.as_view()),
    path('active-session/<pk>/', ActiveSession.as_view()),
    path('dropoutgraduatemanagement/', DropoutGraduateManagementApi.as_view()),


    
]
