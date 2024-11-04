from django.urls import path
from Admin import views
app_name="Admin"
urlpatterns = [
    path('Admin/',views.Admin,name="Admin"),
    path('deleteadmin/<int:id>',views.deleteadmin,name="deleteadmin"),
    

    path('HOD/',views.HOD,name="HOD"),
    path('deletehod/<int:id>',views.deletehod,name="deletehod"),


    path('Course/',views.Course,name="Course"),
    path('deletecourse/<int:id>',views.deletecourse,name="deletecourse"),


    path('Department/',views.Department,name="Department"),
    path('deletedep/<int:id>',views.deletedep,name="deletedep"),

    path('Year/',views.Year,name="Year"),
    path('Year/<int:id>',views.deleteyear,name="deleteyear"),


    path('ActivityType/',views.ActivityType,name="ActivityType"),
    path('ActivityType/<int:id>',views.deleteact,name="deleteact"),
]