from django.urls import path
from .views import *


urlpatterns = [

    path('current-user/', Current_User),
    path('user-list/', UserList.as_view()),
    path('userm-detailed/<id>/', UserDetailed.as_view()),
    # path('resetpasssword/', resetPassword),
    # path('verifyPassword', verifyPassword),
]
