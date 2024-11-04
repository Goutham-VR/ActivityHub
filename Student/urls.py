from django.urls import path
from Student import views
app_name='Student'
urlpatterns = [
    path('ActivityReg/',views.activityreg,name="ActivityReg"),
    path('ViewPoints/',views.viewpoints,name="ViewPoints"),
    path('EditProfile/',views.editprofile,name="EditProfile"),
    path('Myprofile/',views.myprofile,name="Myprofile"),
    path('ChangePassword/',views.changepassword,name="ChangePassword"),
    path('Homepage/',views.homepage,name="Homepage"),
]
