from django.db import models

# Create your models here.
class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=30)
    admin_email=models.CharField(max_length=30)
    admin_password=models.CharField(max_length=30)

class tbl_department(models.Model):
    department_name=models.CharField(max_length=30)

class tbl_activitytype(models.Model):
    activity_name=models.CharField(max_length=30)
    activity_mark=models.CharField(max_length=30)

class tbl_year(models.Model):
    year_name=models.CharField(max_length=30)

class tbl_course(models.Model):
    course_name=models.CharField(max_length=30)
    course_department=models.ForeignKey(tbl_department,on_delete=models.CASCADE)

class tbl_hod(models.Model):
    hod_name=models.CharField(max_length=30)
    hod_email=models.CharField(max_length=30)
    hod_contact=models.CharField(max_length=30)
    hod_photo=models.FileField(upload_to='Assets/Files/HOD')
    hod_password=models.CharField(max_length=30)
    hod_department=models.ForeignKey(tbl_department,on_delete=models.CASCADE)
