# Generated by Django 4.1.7 on 2023-04-20 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0003_delete_login_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('std_class', models.CharField(max_length=100)),
                ('register_num', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(default='d80cf102414d7d87b3073ea9b1ec4ef60a5b59bd5f10a66839f0351d9af1b9ccab08b726817956c6eec1355f97438271e6b42f4e155b7d36fbef23eb6097fc6c', max_length=512)),
                ('register_num', models.CharField(max_length=100, unique=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
