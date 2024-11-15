# Generated by Django 5.1.2 on 2024-10-29 05:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0010_tbl_hod'),
        ('Teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_participation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participation_mark', models.CharField(max_length=30)),
                ('participation_status', models.IntegerField(default=0)),
                ('participation_activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_activitytype')),
                ('participation_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teacher.tbl_student')),
            ],
        ),
    ]
