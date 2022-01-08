# Generated by Django 3.2.6 on 2022-01-08 13:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.PositiveSmallIntegerField(choices=[(1, 'is_superadmin'), (2, 'is_admin'), (3, 'is_coordinator'), (4, 'is_accountant'), (5, 'is_student')], primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, choices=[('IS_SUPERADMIN', 'is_superadmin'), ('IS_ADMIN', 'is_admin'), ('IS_COORDINATOR', 'is_coordinator'), ('IS_ACCOUNTANT', 'is_accountant'), ('IS_STUDENT', 'is_student')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='avtar/')),
                ('father_name', models.CharField(blank=True, max_length=100)),
                ('mother_name', models.CharField(blank=True, max_length=100)),
                ('dob', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('pin_code', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=100, unique=True)),
                ('enrollment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('contact', models.CharField(blank=True, default=0, max_length=100)),
                ('father_email', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_email', models.CharField(blank=True, max_length=100, null=True)),
                ('aadhar_no', models.CharField(blank=True, max_length=100, null=True)),
                ('primary_contact', models.CharField(blank=True, max_length=100, null=True)),
                ('secondary_contact', models.CharField(blank=True, max_length=100, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('gender', models.CharField(blank=True, choices=[('', ''), ('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], default='', max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('roles', models.ForeignKey(blank=True, default=5, on_delete=django.db.models.deletion.CASCADE, to='users.role')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
