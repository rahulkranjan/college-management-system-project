from django.db.models import fields
from account.models import *
from rest_framework import serializers


class AccountHeadSerializers(serializers.ModelSerializer):

    class Meta:
        model = AccountHead
        fields = ('__all__')


class AccountSubHeadSerializers(serializers.ModelSerializer):

    head = AccountHeadSerializers()

    class Meta:
        model = AccountSubHead
        fields = ('__all__')


class AccountSubHeadCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = AccountSubHead
        fields = ('__all__')


class PaymentMethodSerializers(serializers.ModelSerializer):

    class Meta:
        model = PaymentMethod
        fields = ('__all__')


class BankAccountSerializers(serializers.ModelSerializer):

    class Meta:
        model = BankAccount
        fields = ('__all__')


class IncomeSerializers(serializers.ModelSerializer):

    account_sub_head = AccountSubHeadSerializers()
    payment_method = PaymentMethodSerializers()
    bank = BankAccountSerializers()

    class Meta:
        model = Income
        fields = ('__all__')


class IncomeCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Income
        fields = ('__all__')


class ExpenseSerializers(serializers.ModelSerializer):

    account_sub_head = AccountSubHeadSerializers()
    payment_method = PaymentMethodSerializers()
    bank = BankAccountSerializers()

    class Meta:
        model = Expense
        fields = ('__all__')


class ExpenseCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = ('__all__')


class PromocodeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Promocode
        fields = ('__all__')
