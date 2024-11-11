from django.urls import path
from Teacher import views
app_name='Teacher'
urlpatterns = [
    #-----URL---------------Function---------Page----
    path('Homepage/', views.homepage, name='Homepage'),
    path('Student/', views.student, name='Student'),
    path('Myprofile/', views.teacherprofile, name='Myprofile'),
    path('EditProfile/', views.EditProfile, name='EditProfile'),
    path('ChangePassword/',views.ChangePassword, name='ChangePassword'),
    path('Addmark/',views.addmark, name='Addmark'),
    path('mark/<int:id>',views.mark, name='mark'),
    path('AjaxDepartment/',views.AjaxDepartment, name='AjaxDepartment'),
    path('Logout/',views.Logout, name='Logout'),
]
