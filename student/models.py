from django.db import models
from django.db.models.base import Model
from college_data.models import Department, SemesterSession, Session
from users.models import User


# Create your models here.

class StudentProfile(models.Model):
    status_choice = (
        ('current','CURRENT'),
        ('dropout','DROPOUT'),
        ('passout','PASSOUT'),
    )

    religion_choice = (
        ('hindu','HINDU'),
        ('muslim','MUSLIM'),
        ('sikh','SIKH'),
        ('ishi','ISHI'),
    )

    category_choice= (
        ('general','GENERAL'),
        ('ebc','EBC'),
        ('obc','OBC'),
        ('sc','SC'),
        ('st','ST'),
    )
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, blank=True,null=True)
    date_of_admission = models.DateField(blank=True, null=True)
    session_admit = models.ForeignKey(Session, on_delete=models.PROTECT, blank=True,null=True)
    student_status = models.CharField(max_length=50,choices=status_choice, default='current',blank=True)
    student_religion = models.CharField(max_length=50,choices=religion_choice, null=True,blank=True)
    student_category = models.CharField(max_length=50,choices=category_choice, null=True,blank=True)
    
    class Meta:
        db_table = 'student_profile'

    def __str__(self):
        return str(self.user)


class SemesterWiseStudent(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True)
    semester_session = models.ForeignKey(SemesterSession, on_delete= models.CASCADE, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, auto_now=False)    
        
    class Meta:
        db_table = 'semester_wise_student'

    def __str__(self):
        return str(self.user)


class Certificate(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True)
    issue_certificate_name = models.CharField(max_length=200, blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)    
    authority_name = models.CharField(max_length=200, blank=True, null=True)
    attachment = models.FileField(
        upload_to='attachment/', blank=True, null=True)    
    class Meta:
        db_table = 'certificate'

    def __str__(self):
        return str(self.user)
