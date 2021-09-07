# Generated by Django 3.2.7 on 2021-09-07 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210907_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_diagnostic',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_pathology',
        ),
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='college_name',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
        migrations.AddField(
            model_name='user',
            name='education',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='short_info',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
        migrations.AddField(
            model_name='user',
            name='year',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='contact',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=100, unique=True),
        ),
    ]
