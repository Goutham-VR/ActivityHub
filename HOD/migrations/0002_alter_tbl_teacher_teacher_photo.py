# Generated by Django 5.1.2 on 2024-10-24 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOD', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_teacher',
            name='teacher_photo',
            field=models.FileField(upload_to='../Assets/Files/Teacher'),
        ),
    ]
