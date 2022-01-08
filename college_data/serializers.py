from django.db.models import fields
from college_data.models import *
from rest_framework import serializers


class InstituteSerializers(serializers.ModelSerializer):

    class Meta:
        model = Institute
        fields = ('__all__')



class SemesterSerializers(serializers.ModelSerializer):

    class Meta:
        model = Semester
        fields = ('__all__')


class SessionSerializers(serializers.ModelSerializer):

    class Meta:
        model = Session
        fields = ('__all__')



class SemesterSessionSerializers(serializers.ModelSerializer):

    class Meta:
        model = SemesterSession
        fields = ('__all__')




class CourseSerializers(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('__all__')






class DepartmentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ('__all__')


class SemesterSessionInfoSerializers(serializers.ModelSerializer):
    session=SessionSerializers()
    course=CourseSerializers(many=True)
    semester=SemesterSerializers()
    class Meta:
        model = SemesterSession
        fields = ('__all__')


class CourseInfoSerializers(serializers.ModelSerializer):
    department=DepartmentSerializers()
    class Meta:
        model = Course
        fields = ('__all__')