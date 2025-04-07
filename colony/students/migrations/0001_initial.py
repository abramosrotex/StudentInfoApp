# Generated by Django 5.1.4 on 2025-01-23 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=50)),
                ('student_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=50)),
                ('student_address', models.TextField(max_length=1000)),
                ('student_department', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]
