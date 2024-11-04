from django.db import models
from Admin.models import tbl_course

# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=30)
    user_email = models.EmailField()
    user_contact = models.CharField(max_length=15)
    user_address = models.TextField()
    course_department=models.ForeignKey(tbl_course,on_delete=models.CASCADE)
    user_photo = models.FileField(upload_to='../Assets/Files/Student')
    user_password = models.CharField(max_length=100)