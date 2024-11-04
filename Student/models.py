from django.db import models
from Admin.models import tbl_course
from Teacher.models import tbl_student
from Admin.models import tbl_activitytype

# Create your models here.
class tbl_participation(models.Model):
    participation_name=models.CharField(max_length=30)
    participation_activity=models.ForeignKey(tbl_activitytype,on_delete=models.CASCADE)
    participation_student=models.ForeignKey(tbl_student,on_delete=models.CASCADE)
    participation_mark=models.CharField(max_length=30)
    participation_status = models.IntegerField(default=0)