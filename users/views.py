from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserCreateSerializer, UserSerializer, TokenUserSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from django.http import Http404
from rest_framework.renderers import JSONRenderer
from django.template.loader import render_to_string
from rest_framework_jwt.settings import api_settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
import jwt
from django.core.mail import EmailMultiAlternatives


# Create your views here.


@api_view(['GET'])
def Current_User(request):
    serializer = TokenUserSerializer(request.user)
    return Response(serializer.data)


class UserList(ListAPIView):
    # permission_classes = (permissions.IsAuthenticated)
    lookup_field = 'id'
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['email', 'name', 'roles', 'id', 'contact']

    # renderer_classes = [JSONRenderer]

    def get_queryset(self):
        queryset = User.objects.all().order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# user detailed list


class UserDetailed(APIView):
    # permission_classes = (permissions.IsAuthenticated)

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserCreateSerializer(
            user, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# @permission_classes([permissions.AllowAny, ])
# def resetPassword(request):
#     if request.method == 'POST':
#         try:
#             datauser = User.objects.filter(
#                 email=request.data['email'], is_active=True).values()

#             if len(datauser) != 0:

#                 user = User.objects.get(email=request.data['email'])
#                 jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#                 jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
#                 payload = jwt_payload_handler(user)
#                 token = jwt_encode_handler(payload)
#                 recover_link = BASE_URL + "/auth/recover-password/" + \
#                     datauser[0]['email']+"/"+token

#                 text_content = 'Reset password Doctodo Lab'
#                 html_content = render_to_string(
#                     'resetpassword.html', {'recover_link': recover_link, 'name': datauser[0]['name']})
#                 msg = EmailMultiAlternatives('Reset password Doctodo Lab', text_content, EMAIL_VIA, [
#                     request.data['email']])
#                 msg.attach_alternative(html_content, "text/html")
#                 msg.send()
#                 return Response('Email sent', status=status.HTTP_200_OK)
#             return Response('Email sent', status=status.HTTP_204_NO_CONTENT)
#         except:
#             return Response('Except', status=status.HTTP_204_NO_CONTENT)
#     else:
#         return Response("Email Not Found", status=status.HTTP_401_UNAUTHORIZED)


# @api_view(['POST'])
# @permission_classes([permissions.AllowAny, ])
# def verifyPassword(request):
#     if request.method == 'POST':
#         password = request.data['password']
#         userdata = User.objects.filter(
#             email=request.data['email'], is_active=True).values()
#         user = userdata[0]
#         if len(userdata) != 0:
#             try:
#                 user1 = User.objects.get(email=request.data['email'])
#                 payload = jwt.decode(request.data['token'], SECRET_KEY)
#                 email = payload['email']
#                 if request.data['email'] == email:

#                     user1.set_password(password)
#                     user1.save()

#                     text_content = 'Password Changed Successfully Doctodo Lab'
#                     html_content = render_to_string(
#                         'resetsucessful.html', {'name': user['name']})
#                     msg = EmailMultiAlternatives('Password Changed Successfully Doctodo Lab', text_content, EMAIL_VIA, [
#                         request.data['email']])
#                     msg.attach_alternative(html_content, "text/html")
#                     msg.send()
#                     return Response("Your Password is successfully reset")

#                 else:
#                     return Response("Bad Token", status=status.HTTP_400_BAD_REQUEST)
#             except:
#                 return Response('Except', status=status.HTTP_204_NO_CONTENT)

#         else:
#             return Response("User not found", status=status.HTTP_400_BAD_REQUEST)


# class ResetProfilePassword(APIView):
#     def post(self, request):
#         password = request.data['password']
#         if password is not None:
#             user1 = User.objects.get(id=self.request.user.id)
#             if user1:
#                 user1.set_password(password)
#                 user1.save()
#                 text_content = 'Password Changed Successfully Doctodo Lab'
#                 html_content = render_to_string(
#                     'resetsucessful.html', {'name': self.request.user.name})
#                 msg = EmailMultiAlternatives('Password Changed Successfully Doctodo Lab', text_content, EMAIL_VIA, [
#                     self.request.user.email])
#                 msg.attach_alternative(html_content, "text/html")
#                 msg.send()
#                 return Response("Your Password is successfully reset")
#             else:
#                 return Response("Bad Token", status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response("Bad Token", status=status.HTTP_400_BAD_REQUEST)
