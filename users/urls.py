from django.urls import path
from .views import *


urlpatterns = [

    path('current-user/', Current_User),
    path('user/', UserList.as_view()),
    path('user/<pk>/', UserDetailed.as_view()),
    path('bulk-user/', BulkAddUser.as_view()),

]
