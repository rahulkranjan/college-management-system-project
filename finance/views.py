from rest_framework import permissions, status
from rest_framework.generics import ListAPIView
from finance.models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from finance.serializers import *



class FeeTermList(ListAPIView):

    serializer_class = FeeTermSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['term_name', 'status', 'session']

    def get_queryset(self):
        queryset = FeeTerm.objects.filter(
            institute=self.request.user.institute).order_by('id')
        return queryset

    def post(self, request, format=None):
        serializer = FeeTermSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeeTermDetail(APIView):

    def get_object(self, pk):
        try:
            return FeeTerm.objects.get(pk=pk)
        except FeeTerm.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        fee_term = self.get_object(pk)
        serializer = FeeTermSerializers(fee_term)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        fee_term = self.get_object(pk)
        serializer = FeeTermSerializers(fee_term, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        fee_term = self.get_object(pk)
        fee_term.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class FeeTypeList(ListAPIView):

    serializer_class = FeeTypeSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type_name', 'status', 'session']

    def get_queryset(self):
        queryset = FeeType.objects.filter(
            institute=self.request.user.institute).order_by('id')
        return queryset

    def post(self, request, format=None):
        serializer = FeeTypeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeeTypeDetail(APIView):

    def get_object(self, pk):
        try:
            return FeeType.objects.get(pk=pk)
        except FeeType.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        fee_term = self.get_object(pk)
        serializer = FeeTypeSerializers(fee_term)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        fee_term = self.get_object(pk)
        serializer = FeeTypeSerializers(fee_term, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        fee_term = self.get_object(pk)
        fee_term.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class FeeGroupList(ListAPIView):

    serializer_class = FeeGroupSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['institute', 'term_fee', 'status', 'session']

    def get_queryset(self):
        queryset = FeeGroup.objects.filter(
            institute=self.request.user.institute).order_by('id')
        return queryset

    def post(self, request, format=None):
        serializer = FeeGroupSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeeGroupDetail(APIView):

    def get_object(self, pk):
        try:
            return FeeGroup.objects.get(pk=pk)
        except FeeGroup.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        fee_term = self.get_object(pk)
        serializer = FeeGroupSerializers(fee_term)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        fee_term = self.get_object(pk)
        serializer = FeeGroupSerializers(fee_term, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        fee_term = self.get_object(pk)
        fee_term.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

