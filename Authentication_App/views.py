from django.shortcuts import render , redirect
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from django.contrib.auth import login 
from django.http import HttpResponseRedirect

User = get_user_model()



def Login(request):

    email = None
    password = None
    user = None
    users = None


    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        users = User.objects.all()

        for usr in users:
            if usr.email == email and usr.password == password:
                login(request, usr)
                return redirect("home")
                


    
    return render(request , 'login.html')


def Register(request):    
    first_name = None
    last_name = None
    email = None
    password = None
    username = None
    users = None
    pre_url = None
    
    if request.method == 'GET':
        pre_url = request.META.get("HTTP_REFERER")

    
    
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        username = first_name + last_name
        users = User.objects.all()
        new_user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        
        for user in users:
            if user.username == username or  user.email == email :
                print("User already exists")
            else:
                new_user.save()
                login(request, new_user)

                return redirect("home")     




    return render(request, 'register.html')
    

def Logout(request):

    logout(request)

    return redirect("home")


