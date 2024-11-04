from django.db import models
from Admin.models import tbl_hod

# Create your models here.
class tbl_teacher(models.Model):
    teacher_name=models.CharField(max_length=30)
    teacher_email=models.CharField(max_length=30)
    teacher_contact=models.CharField(max_length=30)
    teacher_photo = models.FileField(upload_to='Assets/Files/Teacher')
    teacher_password=models.CharField(max_length=30)
    teacher_hod=models.ForeignKey(tbl_hod,on_delete=models.CASCADE)