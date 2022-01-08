from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.generics import ListAPIView
from staff.models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from staff.serializers import *
from users.serializers import  UserCreateSerializer2, UserSerializerDetailed

# Create your views here.

class CreateStaff(ListAPIView):
    # permission_classes = (permissions.IsAuthenticated)
    serializer_class = UserSerializerDetailed
    queryset = User.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['email', 'name', 'roles', 'id', 'contact']

    # renderer_classes = [JSONRenderer]

    def get_queryset(self):
        queryset = User.objects.all().order_by('-date_joined')
        return queryset

    def post(self, request, format=None):
        if 'staff_profile' in request.data:
            serializer = UserCreateSerializer2(data=request.data)
            if serializer.is_valid():
                user=serializer.save()
                staff_data=request.data['staff_profile']
                staff_data['user']=user.id
                serializer1 = StaffProfileSerializers(data=staff_data)
                if serializer1.is_valid():
                    serializer1.save()
                    return Response("Successfully Created", status=status.HTTP_201_CREATED)
                else:
                    staff_data.delete()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("",status=status.HTTP_400_BAD_REQUEST)



class DesignationList(ListAPIView):

    serializer_class = DesignationSerializers
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['id', 'status']
    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        queryset = Designation.objects.all().order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = DesignationSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DesignationDetail(APIView):
    renderer_classes = [JSONRenderer]

    def get_object(self, pk):
        try:
            return Designation.objects.get(pk=pk)
        except Designation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        designation = self.get_object(pk)
        serializer = DesignationSerializers(designation)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        designation = self.get_object(pk)
        serializer = DesignationSerializers(
            designation, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        designation = self.get_object(pk)
        designation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class StaffProfileList(ListAPIView):

    serializer_class = StaffProfileInfoSerializers
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['id', 'user']
    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        queryset = StaffProfile.objects.all().order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = StaffProfileSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StaffProfileDetail(APIView):
    renderer_classes = [JSONRenderer]

    def get_object(self, pk):
        try:
            return StaffProfile.objects.get(pk=pk)
        except StaffProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        staff_profile = self.get_object(pk)
        serializer = StaffProfileSerializers(staff_profile)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        staff_profile = self.get_object(pk)
        serializer = StaffProfileSerializers(
            staff_profile, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        staff_profile = self.get_object(pk)
        staff_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
