from django.urls import path
from account.views import *
from account.reports import OverallIncomeExpense


urlpatterns = [

    path('accounthead/<pk>', AccountHeadDetail.as_view()),
    path('accounthead/', AccountHeadList.as_view()),
    path('accountsubhead/<pk>', AccountSubHeadDetail.as_view()),
    path('accountsubhead/', AccountSubHeadList.as_view()),
    path('paymentmethod/<pk>', PaymentMethodDetail.as_view()),
    path('paymentmethod/',PaymentMethodList.as_view()),
    path('bankaccount/<pk>', BankAccountDetail.as_view()),
    path('bankaccount/', BankAccountList.as_view()),
    path('income/<pk>', IncomeDetail.as_view()),
    path('income/', IncomeList.as_view()),
    path('expense/<pk>', ExpenseDetail.as_view()),
    path('expense/', ExpenseList.as_view()),
    path('overall-income-expense/', OverallIncomeExpense.as_view()),
    path('promocode/<pk>', PromocodeDetailed.as_view()),
    path('promocode/', PromocodeList.as_view()),
    path('avail-promocode/', PromocodeCheck.as_view()),

]
