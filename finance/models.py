from django.db import models
from college_data.models import Department, Institute, Session


class FeeType(models.Model):

    type_name = models.CharField(
        max_length=100, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    institute = models.ForeignKey(
        Institute, on_delete=models.PROTECT, null=True)
    status = models.BooleanField(default=True)
    session = models.ForeignKey(
        Session, blank=True, null=True, on_delete=models.PROTECT)

    class Meta:
        db_table = 'fee_type'

    def __str__(self):
        return str(self.type_name)


class FeeTerm(models.Model):

    institute = models.ForeignKey(
        Institute, on_delete=models.PROTECT, null=True)
    term_name = models.CharField(max_length=100)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    status = models.BooleanField(default=True)
    session = models.ForeignKey(
        Session, blank=True, null=True, on_delete=models.PROTECT)

    class Meta:
        db_table = 'fee_term'

    def __str__(self):
        return self.term_name


class FeeGroup(models.Model):

    institute = models.ForeignKey(
        Institute, on_delete=models.PROTECT, null=True)
    term_fee = models.ForeignKey(FeeTerm, blank=True, null=True,
                                 on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete= models.PROTECT, blank=True, null=True)

    total_amount = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    session = models.ForeignKey(
        Session, blank=True, null=True, on_delete=models.PROTECT)

    class Meta:
        db_table = 'feeGroup'

    def __str__(self):
        return self.name
