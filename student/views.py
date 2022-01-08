from college_data.models import Institute
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.generics import ListAPIView
from student.models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from student.serializers import *
from users.serializers import UserCreateSerializer, UserCreateSerializer2, UserSerializerDetailed,UserUpdateSerializer


# Create your views here.
def CreateUsername(institute):
    institute=Institute.objects.get(id=institute)
    if institute:
        user=User.objects.all().count()
        username = institute.username_prefix+str(user+1).zfill(7)
        return username

class StudentAdmission(ListAPIView):
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
        if 'student_profile' in request.data:
            if 'username' in request.data:
                if request.data['username'] is None or request.data['username'] =="":
                    username=CreateUsername(self.request.user.institute.id)
                    if username is not None and username !="":
                        request.data['username']=username
                        serializer = UserCreateSerializer(data=request.data)
                        if serializer.is_valid():
                            user=serializer.save(institute=self.request.user.institute.id)
                            student_profile=request.data['student_profile']
                            student_profile['user']=user.id
                            serializer1 = StudentProfilePostSerializers(data=student_profile)
                            if serializer1.is_valid():
                                student = serializer1.save()
                                student_session=request.data['student_session']
                                student_session['user']=user.id
                                serializer2 = SemesterWiseStudentSerializers(data=student_session)
                                if serializer2.is_valid():
                                    serializer2.save()
                                    return Response("successfully Added")
                                else:
                                    student.delete()
                                    return Response(serializer2.errors, status=status.HTTP_400_BAD_REQUEST)
                            else:
                                user.delete()
                                return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)
                        else:
                            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response("failed", status=status.HTTP_400_BAD_REQUEST)
                else:
                    user_check=User.objects.get(username=request.data['username'])
                    if user_check:
                        serializer = UserSerializerDetailed(user_check,request.data, partial=True)
                        if serializer.is_valid():
                            user=serializer.save()
                            student_profile_check=StudentProfile.objects.get(user__username=request.data['username'])
                            if student_profile_check:
                                student_profile=request.data['student_profile']
                                serializer1 = StudentProfilePostSerializers(student_profile_check,student_profile, partial=True)
                                if serializer1.is_valid():
                                    student = serializer1.save()
                                    if 'semester_session' in request.data['student_session']:
                                        student_session=request.data['student_session']
                                        try:
                                            student_session_check=SemesterWiseStudent.objects.get(user__username=request.data['username'],semester_session=student_session['semester_session'])
                                            if student_session_check:
                                                student_session['user']=user.id
                                                serializer2 = SemesterWiseStudentSerializers(student_session_check,student_session, partial=True)
                                                if serializer2.is_valid():
                                                    serializer2.save()
                                                else:
                                                    return Response(serializer2.errors, status=status.HTTP_400_BAD_REQUEST)
                                        except:
                                            student_session=request.data['student_session']
                                            student_session['user']=user.id
                                            serializer3 = SemesterWiseStudentSerializers(data=student_session)
                                            if serializer3.is_valid():
                                                serializer3.save()
                                                return Response("successfully")
                                            else:
                                                return Response(serializer3.errors, status=status.HTTP_400_BAD_REQUEST)
                                else:
                                    return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)
                        else:
                            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response("user not exits", status=status.HTTP_400_BAD_REQUEST)
            else:
                username=CreateUsername(self.request.user.institute.id)
                if username is not None and username !="":
                    request.data['username']=username
                    serializer = UserCreateSerializer(data=request.data)
                    if serializer.is_valid():
                        user=serializer.save()
                        student_profile=request.data['student_profile']
                        student_profile['user']=user.id
                        serializer1 = StudentProfilePostSerializers(data=student_profile)
                        if serializer1.is_valid():
                            student = serializer1.save()
                            student_session=request.data['student_session']
                            student_session['user']=user.id
                            serializer2 = SemesterWiseStudentSerializers(data=student_session)
                            if serializer2.is_valid():
                                serializer2.save()
                                return Response("successfully Added")
                            else:
                                student.delete()
                                return Response(serializer2.errors, status=status.HTTP_400_BAD_REQUEST)
                        else:
                            user.delete()
                            return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response("username not formed", status=status.HTTP_400_BAD_REQUEST)



class StudentProfileList(ListAPIView):

    serializer_class = StudentProfileSerializers
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['id', 'user','department','date_of_admission','user__username','user__enrollment_id','user__contact','student_status']
    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        queryset = StudentProfile.objects.all().order_by('-id')
        return queryset

    def post(self, request, format=None):

        serializer = StudentProfilePostSerializers(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentProfileDetail(APIView):
    renderer_classes = [JSONRenderer]

    def get_object(self, pk):
        try:
            return StudentProfile.objects.get(pk=pk)
        except StudentProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student_profile = self.get_object(pk)
        serializer = StudentProfileSerializers(student_profile)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student_profile = self.get_object(pk)
        serializer = StudentProfilePostSerializers(
            student_profile, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student_profile = self.get_object(pk)
        student_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class SemesterWiseStudentList(ListAPIView):

    serializer_class = SemesterWiseStudentSerializers
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['id', 'semester_session']
    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        queryset = SemesterWiseStudent.objects.all().order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = SemesterWiseStudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SemesterWiseStudentDetail(APIView):
    renderer_classes = [JSONRenderer]

    def get_object(self, pk):
        try:
            return SemesterWiseStudent.objects.get(pk=pk)
        except SemesterWiseStudent.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        semester_wise_student = self.get_object(pk)
        serializer = SemesterWiseStudentSerializers(semester_wise_student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        semester_wise_student = self.get_object(pk)
        serializer = SemesterWiseStudentSerializers(
            semester_wise_student, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        semester_wise_student = self.get_object(pk)
        semester_wise_student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CertificateList(ListAPIView):

    serializer_class = CertificateSerializers
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['id', 'user','issue_certificate_name','authority_name','issue_date']
    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        queryset = Certificate.objects.all().order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = CertificateSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CertificateDetail(APIView):
    renderer_classes = [JSONRenderer]

    def get_object(self, pk):
        try:
            return Certificate.objects.get(pk=pk)
        except Certificate.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        certificate = self.get_object(pk)
        serializer = CertificateSerializers(certificate)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        certificate = self.get_object(pk)
        serializer = CertificateSerializers(
            certificate, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        certificate = self.get_object(pk)
        certificate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActiveSession(APIView):
    def get(self, request, pk, format=None):
        session = Session.objects.get(id=pk)
        if session:
            session.current_session=True
            session.save()
            Session.objects.exclude(id=pk).update(current_session=False)
            return Response("successfully Updated")
        else:
            return Response("Something Went Wrong",status=status.HTTP_400_BAD_REQUEST)
    


class DropoutGraduateManagementApi(APIView):

    def get(self, request, format=None):

        user = self.request.query_params.get('user', None)
        student_status = self.request.query_params.get('student_status', None)
        query = {}
        query1 = {}
        if user != '' and user is not None:
            query['id__in'] = user.split(",")
            query['roles'] = 5
            query1['user__in'] = user.split(",")

        if user is not None and student_status is not None:
            User.objects.filter(**query).update(is_active=0)
            StudentProfile.objects.filter(**query1).update(
                student_status=student_status)
            return Response("Successfully")
        else:
            return Response("Send the required Feilds")