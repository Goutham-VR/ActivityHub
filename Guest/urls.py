from django.urls import path
from Guest import views
app_name="Guest"
urlpatterns = [
    path('Login/',views.login,name="Login"),
    path('',views.index,name="index"),
    path('UserRegistration/',views.user,name="UserRegistration"),
    
]
