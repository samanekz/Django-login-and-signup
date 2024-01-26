from django.urls import path
from . import views

urlpatterns = [
    path ('login_register', views.loginPage, name= "login_register"),

    path ('home', views.home, name="home"),
    path ('register', views.register, name= "register"),
    path ('', views.login, name= "login"),
    path ('dashboard', views.dashbord, name= "dashbord"),
    path ('signup', views.signup, name= "signup")
]