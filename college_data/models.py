from django.db import models

# Create your models here.
class Institute(models.Model):
    college_name = models.CharField(max_length=200, blank=True, null=True)
    college_image = models.ImageField(
        upload_to='college_image/', blank=True, null=True)
    short_name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    background_image = models.ImageField(
        upload_to='college_image/', blank=True, null=True)
    signature = models.ImageField(
        upload_to='college_image/', blank=True, null=True)
    image = models.ImageField(
        upload_to='college_image/', blank=True, null=True)
    username_prefix=models.CharField(max_length=5, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    affilation_no = models.CharField(max_length=200, blank=True, null=True)
    registration_no = models.CharField(max_length=200, blank=True, null=True)
    office_no =  models.CharField(max_length=200, blank=True, null=True)
    website_address = models.CharField(max_length=500, blank=True, null=True)
    api_url = models.CharField(max_length=200, blank=True, null=True)


    class Meta:
        db_table = 'institute'

    def __str__(self):
        return str(self.college_name)

class Semester(models.Model):
    semester_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'semester'

    def __str__(self):
        return str(self.semester_name)

class Session(models.Model):
    session_name = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.BooleanField(default=False,blank=True)
    current_session = models.BooleanField(default=False,blank=True)

    
    class Meta:
        db_table = 'session'

    def __str__(self):
        return str(self.session_name)

class Department(models.Model):
    department_name = models.CharField(max_length=200, blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'department'

    def __str__(self):
        return str(self.department_name)

class Course(models.Model):
    course_name = models.CharField(max_length=200, blank=True, null=True)
    course_code = models.CharField(max_length=10, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete= models.PROTECT, blank=True, null=True)
    status = models.BooleanField(default=True)


    class Meta:
        db_table = 'course'

    def __str__(self):
        return str(self.course_name)


class SemesterSession(models.Model):
    session = models.ForeignKey(Session, on_delete= models.CASCADE, blank=True, null=True)
    semester = models.ForeignKey(Semester, on_delete= models.CASCADE, blank=True, null=True)
    course = models.ManyToManyField(Course)

    class Meta:
        db_table = 'semester_session'

    def __str__(self):
        return str(self.semester)

