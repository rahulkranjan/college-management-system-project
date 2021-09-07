from django.db import models
import uuid
from django.db import models, transaction
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager)
from django.db.models.aggregates import Max
from django.utils import timezone

# Create your models here.


class Role(models.Model):

    IS_SUPERADMIN = 1
    IS_ADMIN = 2
    IS_STUDENT = 3
    IS_TEACHER = 4

    ROLE_CHOICES = (
        (IS_SUPERADMIN, 'is_superadmin'),
        (IS_ADMIN, 'is_admin'),
        (IS_STUDENT, 'is_student'),
        (IS_TEACHER, 'is_teacher')


    )
    ROLES_CHOICES = (
        ('IS_SUPERADMIN', 'is_superadmin'),
        ('IS_ADMIN', 'is_admin'),
        ('IS_STUDENT', 'is_student'),
        ('IS_TEACHER', 'is_teacher')


    )

    id = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, primary_key=True)
    name = models.CharField(
        max_length=100, choices=ROLES_CHOICES, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('roles_id', 1)

        return self._create_user(email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=True)
    roles = models.ForeignKey(Role, on_delete=models.CASCADE, default=3)
    contact = models.BigIntegerField(default=0, )
    address = models.TextField(blank=True, null=True)
    about = models.TextField(blank=True, default='')
    short_info = models.CharField(max_length=120, blank=True, default='')
    education = models.TextField(blank=True, default='')
    college_name = models.CharField(max_length=120, blank=True, default='')
    year = models.CharField(max_length=100, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

    def __str__(self):
        return str(self.email)
