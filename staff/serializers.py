from django.db.models import fields
from college_data.serializers import DepartmentSerializers
from staff.models import *
from rest_framework import serializers
from users.serializers import UserCreateSerializer, UserDetailed



class DesignationSerializers(serializers.ModelSerializer):

    class Meta:
        model = Designation
        fields = ('__all__')



class StaffProfileInfoSerializers(serializers.ModelSerializer):
    user=UserCreateSerializer()
    class Meta:
        model = StaffProfile
        fields = ('__all__')

class StaffProfileSerializers(serializers.ModelSerializer):

    class Meta:
        model = StaffProfile
        fields = ('__all__')