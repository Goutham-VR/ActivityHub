from django.urls import path
from HOD import views
app_name='HOD'
urlpatterns = [
    path('homepage/', views.homepage, name='Homepage'),

    path('MyProfile/', views.hodprofile, name='MyProfile'),
    path('EditProfile/', views.EditProfile, name='EditProfile'),
    path('ChangePassword/', views.ChangePassword, name='ChangePassword'),

    path('Marklist/',views.marklist,name="Marklist"),
    path('VerifyMark/<int:id>',views.verifymark,name="VerifyMark"),
    path('Unverifymark/<int:id>',views.unverifymark,name="Unverifymark"),
    path('Rejectmark/<int:id>',views.rejectmark,name="Rejectmark"),

    path('TeacherReg/',views.TeacherReg,name="TeacherReg"),
    path('deleteteacher/<int:id>',views.deleteteacher,name="deleteteacher"),

]
