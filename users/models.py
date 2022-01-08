
from __future__ import unicode_literals
import uuid
from django.db import models, transaction
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager)

# from college_data.models import Institute


class Role(models.Model):

    IS_SUPERADMIN = 1
    IS_ADMIN = 2
    IS_COORDINATOR = 3
    IS_ACCOUNTANT = 4
    IS_STUDENT = 5

    ROLE_CHOICES = (
        (IS_SUPERADMIN, 'is_superadmin'),
        (IS_ADMIN, 'is_admin'),
        (IS_COORDINATOR, 'is_coordinator'),
        (IS_ACCOUNTANT, 'is_accountant'),
        (IS_STUDENT, 'is_student'),

    )
    ROLES_CHOICES = (
        ('IS_SUPERADMIN', 'is_superadmin'),
        ('IS_ADMIN', 'is_admin'),
        ('IS_COORDINATOR', 'is_coordinator'),
        ('IS_ACCOUNTANT', 'is_accountant'),
        ('IS_STUDENT', 'is_student'),

    )

    id = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, primary_key=True)
    name = models.CharField(
        max_length=100, choices=ROLES_CHOICES, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class UserManager(BaseUserManager):

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        try:
            with transaction.atomic():
                user = self.model(username=username, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('roles_id', 1)

        return self._create_user(username, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    gender_choices = (
        ('', ''),
        ('male', 'MALE'),
        ('female', 'FEMALE'),
        ('other', 'OTHER')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # institute = models.ForeignKey(
    #     Institute, on_delete=models.CASCADE, null=True, related_name='user_institute')
    email = models.EmailField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True)
    roles = models.ForeignKey(
        Role, on_delete=models.CASCADE, default=5, blank=True)
    profile_image = models.ImageField(
        upload_to='avtar/', blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True)
    mother_name = models.CharField(max_length=100, blank=True)
    dob = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True)
    pin_code = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, unique=True)
    enrollment_id = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    contact = models.CharField(max_length=100, blank=True, default=0)
    father_email = models.CharField(max_length=100, blank=True, null=True)
    mother_email = models.CharField(max_length=100, blank=True, null=True)
    aadhar_no = models.CharField(max_length=100, blank=True, null=True)
    primary_contact = models.CharField(max_length=100, blank=True, null=True)
    secondary_contact = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    gender = models.CharField(
        max_length=20, blank=True, default='', choices=gender_choices)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

    def __str__(self):
        return str(self.name)+str(" ") + str(self.username)+str(" ") + str(self.email)
