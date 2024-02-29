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
    return render(request, 'base/home.html')

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
            messages.error(request, 'The username doesn''t exit!')
            return redirect('myLogin')
        user = authenticate(username=username, password=pass1)   
        if user is None:
            messages.error(request, 'password is incorrect')
            return redirect('myLogin')
        login(request, user,)
        fname=user.first_name
        return render(request, "base/home.html", {'fname': fname})        
            
    return render(request, 'base/login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        repass = request.POST.get('repass')

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('signup')
        
        if password != repass:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signup')
        
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, 'Your Account has been successfully created')

        return redirect('myLogin')
    return render(request, 'base/signup.html')


def signout(request):
    logout(request)
    messages.success(request, "Logged out Succeccfully!")
    return redirect('home')