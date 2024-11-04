# Generated by Django 5.1.2 on 2024-10-24 06:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0009_delete_tbl_hod'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_hod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hod_name', models.CharField(max_length=30)),
                ('hod_email', models.CharField(max_length=30)),
                ('hod_contact', models.CharField(max_length=30)),
                ('hod_photo', models.FileField(upload_to='Assets/Files/HOD')),
                ('hod_password', models.CharField(max_length=30)),
                ('hod_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_department')),
            ],
        ),
    ]
