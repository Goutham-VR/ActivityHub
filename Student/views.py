from django.shortcuts import render,redirect
from Student.models import tbl_participation
from Teacher.models import tbl_student
from Admin.models import tbl_activitytype

# Create your views here.
def homepage(request):
    if "sid" in request.session:
        return render(request,'Student/Homepage.html')
    else:
        return redirect("Guest:Login")

#Actvity Reg
def activityreg(request):
    if "sid" in request.session:
        activitytype=tbl_activitytype.objects.all()#select fro dropdown
        student=tbl_student.objects.get(id=request.session['sid'])#for student id
        activity=tbl_participation.objects.filter(participation_student=request.session['sid'])
        if request.method=='POST':
            activity=tbl_activitytype.objects.get(id=request.POST.get('sel_activity'))
            student=tbl_student.objects.get(id=request.session['sid'])
            tbl_participation.objects.create(participation_student=student,participation_activity=activity)
            return redirect("Student:ActivityReg")
        else:
            return render(request,'Student/ActivityReg.html',{'acttype':activitytype,'act':activity})
    else:
        return redirect("Guest:Login")
    
#view Points
def viewpoints(request):
    if "sid" in request.session:
        actpoint=tbl_participation.objects.filter(participation_student=request.session['sid'])
        return render(request,'Student/ViewPoints.html',{'act':actpoint})
    else:
        return redirect("Guest:Login")

#my profile
def myprofile(request):
    if "sid" in request.session:
        student=tbl_student.objects.get(id=request.session['sid'])
        return render(request, 'Student/MyProfile.html',{'std':student})
    else:
        return redirect("Guest:Login")
    

#Edit Profile
def editprofile(request):
    if "sid" in request.session:
        student=tbl_student.objects.get(id=request.session['sid'])
        if request.method=="POST":
            student.student_name=request.POST.get("txt_name")
            student.student_email=request.POST.get("txt_email")
            student.student_contact=request.POST.get("txt_contact")
            student.student_address=request.POST.get("txt_address")
            student.save()
            return render(request,'Student/EditProfile.html',{'msg':"Profile Updated"})
        else:
            return render(request,'Student/EditProfile.html',{'std':student})
    else:
        return redirect("Guest:Login")
    
#Change Password
def changepassword(request):
    if "sid" in request.session:
        student=tbl_student.objects.get(id=request.session['sid'])
        if request.method == "POST":
            if student.student_password == request.POST.get("txt_current"):
                if request.POST.get("txt_pass") == request.POST.get("txt_cpass"):
                    student.student_password = request.POST.get("txt_pass")
                    student.save()
                    return render(request,'Student/ChangePassword.html',{"msg":"Password Updated"})
                else:
                    return render(request,'Student/ChangePassword.html',{"msg1":"Error In Re Password"})
            else:
                return render(request,'Student/ChangePassword.html',{"msg2":"Error In Old Password"})
        else:
            return render(request,'Student/ChangePassword.html')
    else:
        return redirect("Guest:Login")

#Logout
def Logout(request):
    del request.session["sid"]
    return redirect("Guest:Login")