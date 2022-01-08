from django.db.models import fields
from college_data.serializers import DepartmentSerializers, SemesterSessionSerializers
from student.models import *
from rest_framework import serializers

from users.serializers import UserDetailed


class StudentProfileSerializers(serializers.ModelSerializer):
    user = UserDetailed()
    department = DepartmentSerializers()
    class Meta:
        model = StudentProfile
        fields = ('__all__')


class StudentProfilePostSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ('__all__')

class SemesterWiseStudentSerializers(serializers.ModelSerializer):

    class Meta:
        model = SemesterWiseStudent
        fields = ('__all__')



class CertificateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        fields = ('__all__')



