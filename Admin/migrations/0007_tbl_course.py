# Generated by Django 5.1.2 on 2024-10-16 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_alter_tbl_hod_hod_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=30)),
            ],
        ),
    ]