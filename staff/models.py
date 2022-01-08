from django.db import models
from college_data.models import Department, SemesterSession, Session
from users.models import User
# Create your models here.

class Designation(models.Model):
    designation = models.CharField(max_length=200, blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'designation'

    def __str__(self):
        return str(self.designation)

class StaffProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, blank=True,null=True)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, blank=True,null=True) 
    date_of_joining = models.DateField(blank=True, null=True)
    qualification = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'staff_profile'

    def __str__(self):
        return str(self.user)

