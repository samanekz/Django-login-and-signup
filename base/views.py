from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model

# Create your views here.

def loginPage(request):
    if request.method == 'Post':
        username = request.Post.get('username')
        password = request.Post.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user) 
            return redirect('home')  
        else:
            messages.error(request, 'Username Or Password does not exit')
    return render(request, 'base/login_register.html')

def home(request):
    return render(request, 'base/home.html')

def register(request):
    return HttpResponse('register')

def myLogin(request):
    if request.method == 'POST':

        username = request.POST['username']
        pass1 = request.POST['pass']
        user = get_user_model().objects.filter(username=username).first()
        if user is None:
            # user did not exists
            messages.error(request, 'Bad Credentials!')
            return redirect('myLogin')
        user = authenticate(username=username, password=pass1)   
        if user is None:
            messages.error(request, 'password is incorrect')
            return redirect('myLogin')
        login(request, user,)
        fname=user.first_name
        return render(request, "base/login_register.html", {'fname': fname})        
            
    return render(request, 'base/login.html')

def signup(request):
    if request.method == "POST":
       #username = request.POST['username']
       # fname = request.POST['fname']
       # lname = request.POST['lname']
       # email = request.POST['email']
        #password = request.POST['pass']
       # repass = request.POST['repass']
        
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        repass = request.POST.get('repass')


        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, 'Your Account has been successfully created')

        return redirect('login')
    return render(request, 'base/signup.html')

def dashbord(request):
    return HttpResponse('dashbord')

