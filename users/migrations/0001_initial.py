# Generated by Django 3.2.7 on 2021-09-07 14:07

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
                ('id', models.PositiveSmallIntegerField(choices=[(1, 'is_superadmin'), (2, 'is_admin'), (3, 'is_student'), (4, 'is_teacher')], primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, choices=[('IS_SUPERADMIN', 'is_superadmin'), ('IS_ADMIN', 'is_admin'), ('IS_STUDENT', 'is_student'), ('IS_TEACHER', 'is_teacher')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('lab_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('lab_name', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('contact', models.BigIntegerField(default=0, unique=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('roles', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='users.role')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
