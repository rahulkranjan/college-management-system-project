from django.urls import path
from college_data.views import *


urlpatterns = [

    path('institute/<pk>/', InstituteDetail.as_view()),
    # path('institute/', InstituteList.as_view()),
    # path('institute-web/', InstituteWebView.as_view()),
    path('semester/<pk>/', SemesterDetail.as_view()),
    path('semester/', SemesterList.as_view()),
    path('session/<pk>/', SessionDetail.as_view()),
    path('session/', SessionList.as_view()),
    path('semester-session/<pk>/', SemesterSessionDetail.as_view()),
    path('semester-session/', SemesterSessionList.as_view()),
    path('department/', DepartmentList.as_view()),
    path('department/<pk>/', DepartmentDetail.as_view()),
    path('course/', CourseList.as_view()),
    path('course/<pk>/', CourseDetail.as_view()),

]
