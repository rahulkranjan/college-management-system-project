from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.serializers import *
from users.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from django.http import Http404
# Create your views here.


@api_view(['GET'])
def Current_User(request):
    serializer = TokenUserSerializer(request.user)
    return Response(serializer.data)


class UserList(ListAPIView):
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
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailed(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializerDetailed(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializerDetailed(
            user, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BulkAddUser(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request):
        files = request.FILES["user_file"]
        reader = files.read().decode("utf-8")
        lines = reader.split("\n")
        adderuser = []
        for line in lines:
            try:
                fields = line.split(",")
                data_dict = {}
                data_dict["email"] = fields[0]
                data_dict["name"] = fields[1]
                data_dict["password"] = fields[2]
                data_dict["contact"] = fields[3]
                data_dict["username"] = fields[4]
                serializer = UserCreateSerializer(data=data_dict)
                if serializer.is_valid():
                    serializer.save()
                    data_dict["status"] = True
                else:
                    data_dict["status"] = False
                    data_dict["message"] = serializer.errors
                adderuser.append(data_dict)

            except:
                continue
        return Response(adderuser)
