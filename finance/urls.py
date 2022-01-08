from django.urls import path
from finance.views import *


urlpatterns = [

    path('fee-term/', FeeTermList.as_view()),
    path('fee-term/<pk>/', FeeTermDetail.as_view()),
    path('fee-type/', FeeTypeList.as_view()),
    path('fee-type/<pk>/', FeeTypeDetail.as_view()),
    path('fee-group/', FeeGroupList.as_view()),
    path('fee-group/<pk>/',FeeGroupDetail.as_view()),
    

]
