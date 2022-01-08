from rest_framework import permissions, status
from rest_framework.generics import ListAPIView
from account.serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

# Create your views here.


class AccountHeadList(ListAPIView):

    serializer_class = AccountHeadSerializers
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['id', 'status']
    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        queryset = AccountHead.objects.filter(
            user=self.request.user.id).order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = AccountHeadSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountHeadDetail(APIView):
    renderer_classes = [JSONRenderer]

    def get_object(self, pk, user):
        try:
            return AccountHead.objects.get(pk=pk, user=user)
        except AccountHead.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        account_head = self.get_object(pk, self.request.user.id)
        serializer = AccountHeadSerializers(account_head)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        account_head = self.get_object(pk, self.request.user.id)
        serializer = AccountHeadSerializers(
            account_head, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        account_head = self.get_object(pk, self.request.user.id)
        account_head.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AccountSubHeadList(ListAPIView):
    renderer_classes = [JSONRenderer]

    serializer_class = AccountSubHeadSerializers
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['id', 'status', 'types', 'head']

    def get_queryset(self):
        queryset = AccountSubHead.objects.filter(
            head__user=self.request.user.id).order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = AccountSubHeadCreateSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountSubHeadDetail(APIView):
    renderer_classes = [JSONRenderer]

    def get_object(self, pk):
        try:
            return AccountSubHead.objects.get(pk=pk)
        except AccountSubHead.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        account_sub_head = self.get_object(pk)
        serializer = AccountSubHeadCreateSerializers(account_sub_head)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        account_sub_head = self.get_object(pk)
        serializer = AccountSubHeadCreateSerializers(
            account_sub_head, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        account_sub_head = self.get_object(pk)
        account_sub_head.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PaymentMethodList(ListAPIView):
    renderer_classes = [JSONRenderer]

    serializer_class = PaymentMethodSerializers
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['id', 'status']

    def get_queryset(self):
        queryset = PaymentMethod.objects.all().order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = PaymentMethodSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentMethodDetail(APIView):
    renderer_classes = [JSONRenderer]

    def get_object(self, pk):
        try:
            return PaymentMethod.objects.get(pk=pk)
        except PaymentMethod.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        payment_method = self.get_object(pk)
        serializer = PaymentMethodSerializers(payment_method)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        payment_method = self.get_object(pk)
        serializer = PaymentMethodSerializers(
            payment_method, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        payment_method = self.get_object(pk)
        payment_method.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BankAccountList(ListAPIView):
    renderer_classes = [JSONRenderer]

    serializer_class = BankAccountSerializers
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['id', 'status']

    def get_queryset(self):
        queryset = BankAccount.objects.filter(
            user=self.request.user.id).order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = BankAccountSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BankAccountDetail(APIView):
    renderer_classes = [JSONRenderer]

    def get_object(self, pk, user):
        try:
            return BankAccount.objects.get(pk=pk, user=user)
        except BankAccount.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bank_account = self.get_object(pk, self.request.user.id)
        serializer = BankAccountSerializers(bank_account)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bank_account = self.get_object(pk, self.request.user.id)
        serializer = BankAccountSerializers(
            bank_account, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bank_account = self.get_object(pk, self.request.user.id)
        bank_account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class IncomeList(ListAPIView):
    renderer_classes = [JSONRenderer]

    serializer_class = IncomeSerializers
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = {
        'date': ['gte', 'lte', 'exact'],
        'status': ['exact'],
        'id': ['exact'],
        'payment_method': ['exact'],
    }

    def get_queryset(self):
        queryset = Income.objects.filter(
            account_sub_head__head__user=self.request.user.id).order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = IncomeCreateSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IncomeDetail(APIView):
    renderer_classes = [JSONRenderer]

    def get_object(self, pk, user):
        try:
            return Income.objects.get(pk=pk, account_sub_head__head__user=user)
        except Income.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        income = self.get_object(pk, self.request.user.id)
        serializer = IncomeCreateSerializers(income)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        income = self.get_object(pk, self.request.user.id)
        serializer = IncomeCreateSerializers(
            income, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        income = self.get_object(pk, self.request.user.id)
        income.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExpenseList(ListAPIView):
    renderer_classes = [JSONRenderer]

    serializer_class = ExpenseSerializers
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = {
        'date': ['gte', 'lte', 'exact'],
        'status': ['exact'],
        'id': ['exact'],
        'payment_method': ['exact'],
    }

    def get_queryset(self):
        queryset = Expense.objects.filter(
            account_sub_head__head__user=self.request.user.id).order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = ExpenseCreateSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(account_sub_head__head__user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpenseDetail(APIView):
    renderer_classes = [JSONRenderer]

    def get_object(self, pk, user):
        try:
            return Expense.objects.get(pk=pk, account_sub_head__head__user=user)
        except Expense.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        expense = self.get_object(pk, self.request.user.id)
        serializer = ExpenseCreateSerializers(expense)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        expense = self.get_object(pk, self.request.user.id)
        serializer = ExpenseCreateSerializers(
            expense, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        expense = self.get_object(pk, self.request.user.id)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class PromocodeList(ListAPIView):

    serializer_class = PromocodeSerializers
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'promocode']

    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        queryset = Promocode.objects.filter(
            user=self.request.user.id).order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = PromocodeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PromocodeDetailed(APIView):
    renderer_classes = [JSONRenderer]

    def get_object(self, pk, user):
        try:
            return Promocode.objects.get(pk=pk, user=user)
        except Promocode.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        package = self.get_object(pk, self.request.user.id)
        serializer = PromocodeSerializers(package)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        package = self.get_object(pk, self.request.user.id)
        serializer = PromocodeSerializers(
            package, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        package = self.get_object(pk, self.request.user.id)
        package.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PromocodeCheck(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        promocode = self.request.query_params.get('promocode', None)
        if promocode is not None:
            try:
                data=Promocode.objects.filter(promocode=promocode).values()
                if data:
                    return Response(data[0])
                else:
                    return Response({}, status=status.HTTP_400_BAD_REQUEST)
            except Promocode.DoesNotExist:
                return Response({}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
