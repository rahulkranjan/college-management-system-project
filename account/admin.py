from django.contrib import admin
from account.models import *
# Register your models here.
admin.site.register(AccountHead)
admin.site.register(AccountSubHead)
admin.site.register(PaymentMethod)
admin.site.register(BankAccount)
admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(Promocode)
