# Generated by Django 5.1.2 on 2024-10-31 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0011_tbl_district_tbl_place'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_district',
        ),
        migrations.DeleteModel(
            name='tbl_place',
        ),
    ]
