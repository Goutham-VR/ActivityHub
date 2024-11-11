from django.shortcuts import render,redirect
from HOD.models import*
from Admin.models import tbl_course
from Admin.models import tbl_department
from Teacher.models import tbl_student
from Student.models import tbl_participation

# Create your views here.
#Teacher Homepage
def homepage(request):
    if "tid" in request.session:
        return render(request, 'Teacher/Homepage.html')
    else:
        return redirect("Guest:Login")

#Teacher profile
def teacherprofile(request):
    if "tid" in request.session:
        teacher=tbl_teacher.objects.get(id=request.session['tid'])
        return render(request, 'Teacher/MyProfile.html',{'sh':teacher})
    else:
        return redirect("Guest:Login")
    
#Teacher editprofile
def EditProfile(request):
    if "tid" in request.session:
        Teacher=tbl_teacher.objects.get(id=request.session['tid'])
        if request.method == "POST" :
            Teacher.teacher_name = request.POST.get("txt_name")
            Teacher.teacher_address = request.POST.get("txt_address")
            Teacher.teacher_contact = request.POST.get("txt_contact")
            Teacher.teacher_email = request.POST.get("txt_email")
            Teacher.save()
            return render(request,'Teacher/EditProfile.html',{'msg':"Profile Updated"})
        else:
            return render(request,'Teacher/EditProfile.html',{'sh':Teacher})
    else:
        return redirect("Guest:Login")
    

#Teacher changepassword
def ChangePassword(request):
    if "tid" in request.session:
        teacher=tbl_teacher.objects.get(id=request.session['tid'])
        if request.method == "POST":
            if teacher.teacher_password == request.POST.get("txt_current"):
                if request.POST.get("txt_pass") == request.POST.get("txt_cpass"):
                    teacher.teacher_password = request.POST.get("txt_pass")
                    teacher.save()
                    return render(request,'Teacher/ChangePassword.html',{"msg":"Profile Updated"})
                else:
                    return render(request,'Teacher/ChangePassword.html',{"msg1":"Error In Re Password"})
            else:
                return render(request,'Teacher/ChangePassword.html',{"msg1":"Error In Old Password"})
        else:
            return render(request,'Teacher/ChangePassword.html')
    else:
        return redirect("Guest:Login")
    

#View Mark
def addmark(request):
    if "tid" in request.session:
        participation=tbl_participation.objects.filter(participation_status=0)#select qry
        return render(request,'Teacher/Addmark.html',{'ptn':participation}) 
    else:
        return redirect("Guest:Login")
       

#Activity Point
def mark(request,id):
    if "tid" in request.session:
        mark=tbl_participation.objects.get(id=id)
        if request.method == "POST":
            mark.participation_mark = request.POST.get("txt_mark")
            mark.save()
            return render(request,'Teacher/Mark.html',{'msg':"mark Updated"})
        else:
            return render(request,'Teacher/Mark.html',{'sh':mark})
    else:
        return redirect("Guest:Login")
    

#Student Registration
def student(request):
    if "tid" in request.session:
        course=tbl_course.objects.all()#select for dropdown
        department=tbl_department.objects.all()#select for dropdown
        if request.method=='POST':
            name=request.POST.get('txt_name')
            email=request.POST.get('txt_email')
            contact=request.POST.get('txt_contact')
            address=request.POST.get('txt_address')
            course=tbl_course.objects.get(id=request.POST.get('sel_course'))#for dropdown
            department=tbl_department.objects.get(id=request.POST.get('sel_department'))#for dropdown
            photo=request.FILES.get('txt_photo')
            password=request.POST.get('txt_password')
            cpass=request.POST.get('txt_cpass')
            if cpass==password:
                tbl_student.objects.create(student_name=name,student_email=email,student_contact=contact,student_address=address,
                student_course=course,student_department=department,student_photo=photo,student_password=password)
                return redirect("Teacher:Student")
            else:
                print("Password Not Match")
                return render(request,'Teacher/Student.html')
        return render(request,'Teacher/Student.html',{'course':course,'dep':department})
    else:
        return redirect("Guest:Login")
    

#ajax
def AjaxDepartment(request):
    coursedata=tbl_course.objects.filter(course_department=request.GET.get('deptid'))
    return render(request,"Teacher/Ajaxdepartment.html",{'data':coursedata})

#Logout
def Logout(request):
    del request.session["tid"]
    return redirect("Guest:Login")