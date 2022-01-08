from rest_framework import permissions, status
from rest_framework.generics import ListAPIView
from college_data.models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from college_data.serializers import *
# from college_management.settings import MEDIA_ROOT


# class InstituteWebView(APIView):
#     serializer_class = InstituteSerializers
#     filter_backends = [DjangoFilterBackend, ]
#     filterset_fields = ['id', 'college_name']
#     renderer_classes = [JSONRenderer]
#     permission_classes = (permissions.AllowAny,)

#     def get(self, request, format=None):
#         id = self.request.query_params.get('id', None)
#         if id is not None:
#             queryset = Institute.objects.filter(id=id).values().order_by('-id')
#             if queryset:
#                 if 'college_image' in queryset[0]:
#                     queryset[0]['college_image']=MEDIA_ROOT+queryset[0]['college_image']
#                 if 'background_image' in queryset[0]:
#                     queryset[0]['background_image']=MEDIA_ROOT+queryset[0]['background_image']
#                 if 'signature' in queryset[0]:
#                     queryset[0]['signature']=MEDIA_ROOT+queryset[0]['signature']
#                 if 'image' in queryset[0]:
#                     queryset[0]['image']=MEDIA_ROOT+queryset[0]['image']

#                 return Response(queryset[0])
#             else:
#                 return Response({}, status=status.HTTP_400_BAD_REQUEST)


# class InstituteList(APIView):

#     serializer_class = InstituteSerializers
#     filter_backends = [DjangoFilterBackend, ]
#     filterset_fields = ['id', 'college_name']
#     renderer_classes = [JSONRenderer]

#     def get(self, request, format=None):
#         queryset = Institute.objects.filter(user_institute = self.request.user).values().order_by('-id')
#         if queryset:
#             if 'college_image' in queryset[0]:
#                 queryset[0]['college_image']=MEDIA_ROOT+queryset[0]['college_image']
#             if 'background_image' in queryset[0]:
#                 queryset[0]['background_image']=MEDIA_ROOT+queryset[0]['background_image']
#             if 'signature' in queryset[0]:
#                 queryset[0]['signature']=MEDIA_ROOT+queryset[0]['signature']
#             if 'image' in queryset[0]:
#                 queryset[0]['image']=MEDIA_ROOT+queryset[0]['image']

#             return Response(queryset[0])
#         else:
#             return Response({}, status=status.HTTP_400_BAD_REQUEST)


#     def post(self, request, format=None):
#         serializer = InstituteSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InstituteDetail(APIView):
    renderer_classes = [JSONRenderer]

    def get_object(self, pk):
        try:
            return Institute.objects.get(pk=pk)
        except Institute.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        institute = self.get_object(pk)
        serializer = InstituteSerializers(institute)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        institute = self.get_object(pk)
        serializer = InstituteSerializers(
            institute, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        institute = self.get_object(pk)
        institute.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SemesterList(ListAPIView):

    serializer_class = SemesterSerializers
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['id', 'semester_name']
    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        queryset = Semester.objects.all().order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = SemesterSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SemesterDetail(APIView):
    renderer_classes = [JSONRenderer]

    def get_object(self, pk):
        try:
            return Semester.objects.get(pk=pk)
        except Semester.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        semester = self.get_object(pk)
        serializer = SemesterSerializers(semester)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        semester = self.get_object(pk)
        serializer = SemesterSerializers(
            semester, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        semester = self.get_object(pk)
        semester.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SessionList(ListAPIView):

    serializer_class = SessionSerializers
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['id', 'session_name', 'start_date', 'end_date']
    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        queryset = Session.objects.all().order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = SessionSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SessionDetail(APIView):
    renderer_classes = [JSONRenderer]

    def get_object(self, pk):
        try:
            return Session.objects.get(pk=pk)
        except Session.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        session = self.get_object(pk)
        serializer = SessionSerializers(session)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        session = self.get_object(pk)
        serializer = SessionSerializers(
            session, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        session = self.get_object(pk)
        session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SemesterSessionList(ListAPIView):

    serializer_class = SemesterSessionInfoSerializers
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['id', 'session', 'semester', 'course']
    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        queryset = SemesterSession.objects.all().order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = SemesterSessionSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SemesterSessionDetail(APIView):
    renderer_classes = [JSONRenderer]

    def get_object(self, pk):
        try:
            return SemesterSession.objects.get(pk=pk)
        except SemesterSession.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        semester_session = self.get_object(pk)
        serializer = SemesterSessionSerializers(semester_session)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        semester_session = self.get_object(pk)
        serializer = SemesterSessionSerializers(
            semester_session, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        semester_session = self.get_object(pk)
        semester_session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseList(ListAPIView):

    serializer_class = CourseInfoSerializers
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['id', 'course_name', 'course_code']
    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        queryset = Course.objects.all().order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = CourseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetail(APIView):
    renderer_classes = [JSONRenderer]

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        course = self.get_object(pk)
        serializer = CourseSerializers(course)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        course = self.get_object(pk)
        serializer = CourseSerializers(
            course, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DepartmentList(ListAPIView):

    serializer_class = DepartmentSerializers
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['id', 'department_name']
    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        queryset = Department.objects.all().order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = DepartmentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentDetail(APIView):
    renderer_classes = [JSONRenderer]

    def get_object(self, pk):
        try:
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        department = self.get_object(pk)
        serializer = DepartmentSerializers(department)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        department = self.get_object(pk)
        serializer = DepartmentSerializers(
            department, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        department = self.get_object(pk)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
