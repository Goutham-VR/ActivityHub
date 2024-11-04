from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import tbl_hod
from Admin.models import tbl_course
from HOD.models import tbl_teacher
from Teacher.models import tbl_student
# Create your views here.

def index(request):
    return render(request,'Guest/index.html')

#Login Block HOD--------------------------------------------------------------------------------#
def login(request):
    if request.method=="POST":
        email=request.POST.get('txt_email')
        password=request.POST.get('txt_password')
        hodcount = tbl_hod.objects.filter(hod_email=email,hod_password=password).count()
        teachercount = tbl_teacher.objects.filter(teacher_email=email,teacher_password=password).count()
        studentcount = tbl_student.objects.filter(student_email=email,student_password=password).count()
        if hodcount > 0 :
            hod = tbl_hod.objects.get(hod_email=email, hod_password=password)
            request.session["hid"] = hod.id
            print(hod.id)
            return redirect("HOD:Homepage")
        elif teachercount >0:
            teacher = tbl_teacher.objects.get(teacher_email=email, teacher_password=password)
            request.session["tid"] = teacher.id
            print(teacher.id)
            return redirect("Teacher:Homepage")
        elif studentcount > 0:
            student=tbl_student.objects.get(student_email=email, student_password=password)
            request.session['sid'] = student.id
            print(student.id)
            return redirect("Student:Homepage")
        else:
            return render(request, 'Guest/Login.html', {"msg":"invalid Data"})
    else:
        return render(request,'Guest/Login.html')


#user block---------------------------------------------------------------------------------#
def user(request):
    course=tbl_course.objects.all()#select for dropdown
    if request.method=='POST':
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_contact')
        address=request.POST.get('txt_address')
        course=tbl_course.objects.get(id=request.POST.get('sel_course'))#for dropdown
        photo=request.POST.get('txt_photo')
        password=request.POST.get('txt_password')
        cpass=request.POST.get('txt_cpass')
        if cpass==password:
            tbl_user.objects.create(user_name=name,user_email=email,user_contact=contact,user_address=address,
            course_department=course,user_photo=photo,user_password=password)
            return redirect("Guest:UserRegistration")
        else:
            print("Password Not Match")
            return render(request,'Guest/UserRegistration.html')
    return render(request,'Guest/UserRegistration.html',{'course':course})
        
