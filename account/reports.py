import datetime
from datetime import timedelta

import pandas as pd
from django.db.models import FloatField, Sum
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import *


class OverallIncomeExpense(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):

        lte_date = self.request.query_params.get('lte_date', None)
        gte_date = self.request.query_params.get('gte_date', None)
        account_sub_head = self.request.query_params.get(
            'account_sub_head', None)
        head = self.request.query_params.get('head', None)
        account_check = self.request.query_params.get('account_check', True)
        lab = self.request.query_params.get('lab', None)
        queryincomeexpense = {}

        if head != '' and head is not None:
            queryincomeexpense['account_sub_head__head__in'] = head.split(
                ",")

        if account_sub_head != '' and account_sub_head is not None:
            queryincomeexpense['account_sub_head__in'] = account_sub_head.split(
                ",")

        # if lab != '' and lab is not None:
        #     queryincomeexpense['account_sub_head__head__lab'] = lab.split(
        #         ",")

        d = []
        if self.request.user is not None and lte_date is not None and gte_date is not None:
            month_list = pd.date_range(
                start=gte_date, end=lte_date, freq='M')
            for j in month_list:
                if account_check == True or account_check == "true":
                    queryset = Income.objects.filter(account_sub_head__head__lab=self.request.user.id, date__month=j.strftime('%m'), date__year=int(
                        j.strftime('%Y')), **queryincomeexpense, status=True).aggregate(total_amount=Sum('amount', output_field=FloatField()))
                    queryset1 = Expense.objects.filter(
                        account_sub_head__head__lab=self.request.user.id,
                        date__month=j.strftime('%m'), date__year=int(j.strftime('%Y')), **queryincomeexpense, status=True).aggregate(total_amount=Sum('amount', output_field=FloatField()))
                else:
                    queryset = {'total_amount': 0}
                    queryset1 = {'total_amount': 0}

                d.append({'month': j.strftime('%B'), 'year': int(j.strftime(
                    '%y')), 'income': queryset['total_amount'], 'expense': queryset1['total_amount']})

            return Response(d)
        else:

            return Response("No data")
