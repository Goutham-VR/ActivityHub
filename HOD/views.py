from django.shortcuts import render,redirect,get_object_or_404
from HOD.models import*
from Admin.models import tbl_hod
from HOD.models import tbl_teacher
from Student.models import tbl_participation
# Create your views here.
#HOD Homepage
def homepage(request):
    return render(request, 'HOD/Homepage.html')

#HOD profile
def hodprofile(request):
    hod=tbl_hod.objects.get(id=request.session['hid'])
    return render(request, 'HOD/MyProfile.html',{'sh':hod})

#HOD editprofile
def EditProfile(request):
    HOD=tbl_hod.objects.get(id=request.session['hid'])
    if request.method == "POST" :
         HOD.hod_name = request.POST.get("txt_name")
         HOD.hod_address = request.POST.get("txt_address")
         HOD.hod_contact = request.POST.get("txt_contact")
         HOD.hod_email = request.POST.get("txt_email")
         HOD.save()
         return render(request,'HOD/EditProfile.html',{'msg':"Profile Updated"})
    else:
         return render(request,'HOD/EditProfile.html',{'hod':HOD})

#HOD changepassword
def ChangePassword(request):
    hod=tbl_hod.objects.get(id=request.session['hid'])
    if request.method == "POST":
        if hod.hod_password == request.POST.get("txt_current"):
            if request.POST.get("txt_pass") == request.POST.get("txt_cpass"):
               hod.hod_password = request.POST.get("txt_pass")
               hod.save()
               return render(request,'HOD/ChangePassword.html',{"msg":"Profile Updated"})
            else:
               return render(request,'HOD/ChangePassword.html',{"msg1":"Error In Re Password"})
        else:
            return render(request,'HOD/ChangePassword.html',{"msg1":"Error In Old Password"})
    else:
        return render(request,'HOD/ChangePassword.html')

#HOD Activitypointverify
#ACCEPT REJECT
def marklist(request):
    unverified=tbl_participation.objects.filter(participation_status=0, participation_mark__isnull=False).exclude(participation_mark="")
    verified=tbl_participation.objects.filter(participation_status=1)
    rejectedverified=tbl_participation.objects.filter(participation_status=2)
    return render(request, 'HOD/ActivityPointVerify.html',{'un':unverified,'ver':verified,'unv':rejectedverified})

def verifymark(request,id):
    accept = tbl_participation.objects.get(id=id)
    accept.participation_status = 1
    accept.save()
    msg = "Approved"
    return redirect("HOD:Marklist")

def unverifymark(request,id):
    unverify = tbl_participation.objects.get(id=id)
    unverify.participation_status = 0
    unverify.save()
    msg = "Rejected"
    return redirect("HOD:Marklist")

def rejectmark(request,id):
    reject = tbl_participation.objects.get(id=id)
    reject.participation_status = 2
    reject.save()
    msg = "Rejected"
    return redirect("HOD:Marklist")

#Teacher Regostration
def TeacherReg(request):
    teacher=tbl_teacher.objects.all()
    if request.method=='POST':
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_contact')
        password=request.POST.get('txt_password')
        photo=request.FILES.get('txt_photo')
        hodid=tbl_hod.objects.get(id=request.session['hid'])
        tbl_teacher.objects.create(teacher_name=name,teacher_email=email,teacher_contact=contact,teacher_photo=photo,teacher_password=password,teacher_hod=hodid)
        return redirect("HOD:TeacherReg")
    else:
        return render(request,'HOD/TeacherReg.html',{'tr':teacher})

#Teacher Delete
def deleteteacher(request,id):
    tbl_teacher.objects.get(id=id).delete()
    return redirect("HOD:TeacherReg")
