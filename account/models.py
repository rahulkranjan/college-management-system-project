from django.db import models
from users.models import User


class AccountHead(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True)
    head = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'account_head'

    def __str__(self):
        return str(self.head)


class AccountSubHead(models.Model):

    type_choices = (
        ('income', 'INCOME'),
        ('expense', 'EXPENSE')
    )
    head = models.ForeignKey(
        AccountHead, blank=True, null=True, on_delete=models.PROTECT, limit_choices_to={'status': True})
    subhead = models.CharField(max_length=100)
    types = models.CharField(
        max_length=50, choices=type_choices, default='income')
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'account_subhead'

    def __str__(self):
        return str(self.subhead) + "-" + str(self.head)


class PaymentMethod(models.Model):
    CASH = 1
    ONLINE = 2
    CHEQUE = 3
    UPI = 4
    RAZORPAY = 5
    PAYTM = 6
    GPAY = 7
    PHONEPE = 8
    BHIM = 9

    TYPE_CHOICES = (
        (CASH, 'cash'),
        (ONLINE, 'online'),
        (CHEQUE, 'cheque'),
        (UPI, 'upi'),
        (RAZORPAY, 'razorpay'),
        (PAYTM, 'paytm'),
        (GPAY, 'gpay'),
        (PHONEPE, 'phonepe'),
        (BHIM, 'bhim'),
    )

    TYPES_CHOICES = (
        ('CASH', 'cash'),
        ('ONLINE', 'online'),
        ('CHEQUE', 'cheque'),
        ('UPI', 'upi'),
        ('RAZORPAY', 'razorpay'),
        ('PAYTM', 'paytm'),
        ('GPAY', 'gpay'),
        ('PHONEPE', 'phonepe'),
        ('BHIM', 'bhim'),
    )

    id = models.PositiveSmallIntegerField(
        choices=TYPE_CHOICES, primary_key=True)
    payment_method = models.CharField(
        max_length=100, choices=TYPES_CHOICES, blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'payment_method'

    def __str__(self):
        return str(self.payment_method)


class BankAccount(models.Model):

    bank_choices = (
        ('pettycash', 'PETTYCASH'),
        ('bank', 'BANK'),
    )
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True)
    account_name = models.CharField(max_length=200, default='')
    opening_balance = models.FloatField()
    total_balance = models.FloatField(default=0)
    account_type = models.CharField(max_length=200, blank=True,
                                    null=True, choices=bank_choices)
    note = models.TextField(blank=True,null=True,)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'bank_account'

    def __str__(self):
        return str(self.account_name)


class Income(models.Model):

    name = models.CharField(max_length=100, default='')
    account_sub_head = models.ForeignKey(
        AccountSubHead, blank=True, null=True, on_delete=models.PROTECT, limit_choices_to={'status': True})
    payment_method = models.ForeignKey(
        PaymentMethod, blank=True, null=True, on_delete=models.PROTECT, limit_choices_to={'status': True})
    bank = models.ForeignKey(BankAccount, blank=True,
                             null=True, on_delete=models.PROTECT)
    date = models.DateField()
    created_date = models.DateField(auto_now_add=True, auto_now=False)
    amount = models.FloatField(default=0)
    file = models.FileField(upload_to='file/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'income'

    def __str__(self):
        return str(self.name)


class Expense(models.Model):

    name = models.CharField(max_length=100, default='')
    account_sub_head = models.ForeignKey(
        AccountSubHead, blank=True, null=True, on_delete=models.PROTECT, limit_choices_to={'status': True})
    payment_method = models.ForeignKey(
        PaymentMethod, blank=True, null=True, on_delete=models.PROTECT, limit_choices_to={'status': True})
    bank = models.ForeignKey(BankAccount, blank=True,
                             null=True, on_delete=models.PROTECT)
    date = models.DateField()
    created_date = models.DateField(auto_now_add=True, auto_now=False)
    amount = models.FloatField()
    file = models.FileField(upload_to='file/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'expense'

    def __str__(self):
        return str(self.name)


class Promocode(models.Model):
    promocode = models.CharField(max_length=100, null=True, blank=True)
    value = models.FloatField(default=0, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True)
    count = models.CharField(max_length=100, null=True, blank=True)
    till_date = models.DateField(blank=True, null=True)
    is_percentage = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    class Meta:
        db_table = 'promocode'

    def __str__(self):
        return str(self.promocode)