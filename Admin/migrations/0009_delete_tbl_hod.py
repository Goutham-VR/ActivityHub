# Generated by Django 5.1.2 on 2024-10-24 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_tbl_course_course_department'),
        ('HOD', '0004_delete_tbl_teacher'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_hod',
        ),
    ]
