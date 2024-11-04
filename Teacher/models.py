from django.db import models
from Admin.models import tbl_course
from Admin.models import tbl_department

# Create your models here.
class tbl_student(models.Model):
    student_name=models.CharField(max_length=30)
    student_email = models.EmailField()
    student_contact = models.CharField(max_length=15)
    student_address = models.TextField()
    student_course=models.ForeignKey(tbl_course,on_delete=models.CASCADE)
    student_department=models.ForeignKey(tbl_department,on_delete=models.CASCADE)
    student_photo = models.FileField(upload_to='Assets/Files/Student')
    student_password = models.CharField(max_length=100)