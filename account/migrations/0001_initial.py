# Generated by Django 3.2.20 on 2023-07-13 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=65)),
                ('fname', models.CharField(default='', max_length=65)),
                ('date_of_birth', models.DateField(default=datetime.datetime.now)),
                ('address', models.TextField()),
                ('user_name', models.CharField(default='', max_length=65)),
                ('password', models.CharField(default='', max_length=40)),
            ],
            options={
                'db_table': 'parent',
            },
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=65)),
                ('fname', models.CharField(default='', max_length=65)),
                ('date_of_birth', models.DateField(default=datetime.datetime.now)),
                ('address', models.TextField()),
                ('username', models.CharField(default='', max_length=65)),
                ('password', models.CharField(default='', max_length=40)),
                ('avtive', models.BooleanField(default=True)),
                ('phone', models.CharField(default='', max_length=13)),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=65)),
                ('fname', models.CharField(default='', max_length=65)),
                ('date_of_birth', models.DateField(default=datetime.datetime.now)),
                ('address', models.TextField()),
                ('toifa', models.CharField(choices=[('OM', "Oliy Ma'lumot"), ('OR', "O'rta Ma'lumot"), ('OP', "O'qituvchi Pedagok")], default='', max_length=2)),
                ('salary', models.PositiveIntegerField(default=1)),
                ('school', models.ManyToManyField(to='school.SchoolModel')),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
    ]
