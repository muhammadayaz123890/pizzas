from django.shortcuts import render
from django.http import JsonResponse
from .models import Subscription
import random
import string 
from django.http import HttpResponse
from io import BytesIO
from Src_App.models import Food

def Random_Api_key(length):
    
    letters = string.ascii_lowercase
    
    result_str = ''.join(random.choice(letters) for i in range(length))

    return  result_str



def Developer_Console_Home(request):

    return render(request , 'api_console_home.html')


def Subscribe(request):

    try:
        

        context = {}
        context['text'] = text
        subscriptions = Subscription.objects.all()


        for sub in subscriptions:
            if sub.user == request.user:
                text = 'Unsubscribe'
                context['text'] = text


        if request.method == 'GET':
            plan = request.GET.get("plan")
            if plan:
                context['plan'] = plan
        
    except:
        pass

    return render(request , 'api_subscribe.html' , context)


def Subscribe_to_plan(request):

    context = {}
    user = None
    key = Random_Api_key(50)
    context['key'] = key
    try:
        if request.user != "AnonymousUser":
            if request.method == 'GET':
                user = request.user
                if Subscription.objects.filter(user=request.user).exists():
                    print("Sorry already exits")
                    context['key'] = "None"
                elif Subscription.objects.filter(key=key):
                    print("")
                else:
                    print("Good till this")
                    new_sub = Subscription.objects.create(
                        user=request.user,
                        key=key + request.user.first_name,
                        payment=False,
                        plan=request.GET.get("sub")
                    )
                    new_sub.save()
        elif request.user == 'AnonymousUser':
            print("Nope!")
            return JsonResponse({"Done" : "cannot subscribe to this api without setting an account."})

    except Exception as E:
        print(E)
        
    return JsonResponse({"key" : key})


def Get_Data(request):

    subn = None
    foods = Food.objects.values()
    foods = list(foods)
    if request.method == 'GET':
        api_key = request.GET.get("api_key")
        print(api_key)

        try:
            subn = Subscription.objects.get(key=api_key)    
        except:
            pass

        if subn:
            subn.requests_per_day += 1
            subn.save()

            return JsonResponse({"Foods" : foods})
        if not subn:
            return JsonResponse({
                "Error" : "Please subscribe to the Pizzerios API and use your valid API key to retrieve the data.",
            })

    return JsonResponse({"Data" : "This is your required JsonResponse data"})