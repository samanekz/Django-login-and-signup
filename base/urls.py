from django.urls import path
from . import views

urlpatterns = [
    path ('login_register', views.loginPage, name= "login_register"),

    path ('', views.home, name="home"),
    path ('register', views.register, name= "register"),
    path ('myLogin', views.myLogin, name= "myLogin"),
    path('signout', views.signout, name='signout'),
    path ('signup', views.signup, name= "signup")
]