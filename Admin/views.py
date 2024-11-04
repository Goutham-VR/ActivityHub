from django.shortcuts import render,redirect
from Admin.models import *
# Create your views here.
#Admin Block--------------------------------------------------------------------------------#
#insert, select
def Admin(request):
    admin=tbl_admin.objects.all()
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        pwd=request.POST.get('txt_password')
        tbl_admin.objects.create(admin_name=name,admin_email=email,admin_password=pwd)
        return render(request,"Admin/Admin.html")
    else:
        return render(request,'Admin/Admin.html',{'ad':admin})
#delete
def deleteadmin(request, id):
    tbl_admin.objects.get(id=id).delete()
    return redirect("Admin:Admin")

#HOD BLOCK----------------------------------------------------------------------------------------#
#Insert Select
def HOD(request):
    department=tbl_department.objects.all()#select for dropdown
    hod=tbl_hod.objects.all()#select
    if request.method=='POST':
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_contact')
        photo=request.FILES.get('txt_photo')
        password=request.POST.get('txt_password')
        department=tbl_department.objects.get(id=request.POST.get('sel_department'))#for dropdown
        tbl_hod.objects.create(hod_name=name,hod_email=email,hod_contact=contact,hod_photo=photo,hod_password=password,hod_department=department)
        return redirect("Admin:HOD")
    else:
        return render(request,'Admin/HOD.html',{'dep':department,'HOD':hod})
#delete
def deletehod(request,id):
    tbl_hod.objects.get(id=id).delete()
    return redirect("Admin:HOD")

#Course Block-------------------------------------------------------------------------------------#
#insert select
def Course(request):
    course=tbl_course.objects.all()#select
    department=tbl_department.objects.all()#for dep drop down
    if request.method=='POST':
        course=request.POST.get('txt_course')
        department=tbl_department.objects.get(id=request.POST.get('sel_department'))
        tbl_course.objects.create(course_name=course,course_department=department)
        return redirect("Admin:Course")
    else:
        return render(request,'Admin/Course.html',{'dep':department,'course':course})
#delete
def deletecourse(request,id):
    tbl_course.objects.get(id=id).delete()
    return redirect("Admin:Course")

#Department Block---------------------------------------------------------------------------------#
#insert select
def Department(request):
    dep=tbl_department.objects.all()#select
    if request.method=="POST":
        department=request.POST.get('txt_department')
        tbl_department.objects.create(department_name=department)
        return render(request,'Admin/Department.html')
    else:
        return render(request,'Admin/Department.html',{'dep':dep})
#delete
def deletedep(request,id):
    tbl_department.objects.get(id=id).delete()
    return redirect("Admin:Department")

#Year Block---------------------------------------------------------------------------------------#
def Year(request):
    year=tbl_year.objects.all()
    if request.method=='POST':
        year=request.POST.get('txt_year')
        tbl_year.objects.create(year_name=year)
        return render(request,'Admin/Year.html')
    else:
        return render(request,'Admin/Year.html',{'data':year})
#delete
def deleteyear(request,id):
    tbl_year.objects.get(id=id).delete()
    return redirect("Admin:Year")

#Activity Block------------------------------------------------------------------------------------#
def ActivityType(request):
    act=tbl_activitytype.objects.all()
    if request.method=="POST":
        activity=request.POST.get('txt_activity')
        mark=request.POST.get('txt_mark')
        tbl_activitytype.objects.create(activity_name=activity, activity_mark=mark)
        return render(request,'Admin/ActivityType.html')
    else:
        return render(request,'Admin/ActivityType.html',{'act':act})
#delete
def deleteact(request,id):
    tbl_activitytype.objects.get(id=id).delete()
    return redirect("Admin:ActivityType")