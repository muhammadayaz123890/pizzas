from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Food, Food_Categorie
import json
from django.http import JsonResponse
from rest_framework.serializers import ModelSerializer


def Home(request):
    context = {}
    all_categories = None
    foods = Food.objects.all()
    all_categories = Food_Categorie.objects.all()



    context['foods'] = foods
    
    category_names = []

    for category in all_categories:
        category_names.append(category.category_name)

        context['categories'] = category_names
    

    return render(request , 'index.html' , context)



#################### FOR SEARCH OF THE FOODS ####################################


def Search(request):

    context = {}
    name_list = []

    if request.method == 'GET':
        name = request.GET.get('food_name')
        if name:

            foods = Food.objects.filter(name__icontains=name).values()
            foods = list(foods)
            for food in foods:

                food_object = {}
                food_object['id'] =  food['id'] 
                food_object['name'] = food['name']                
                name_list.append(food_object)

    return JsonResponse({"Foods" : name_list})




def Ajax_Data(request):
    category = None
    if request.method == 'GET':
        name = request.GET.get("cat_name")
        category = Food_Categorie.objects.get(category_name=name)
        if category:
            foods = Food.objects.filter(category=category).values()
            foods = list(foods)
            print(foods)    

    return JsonResponse({"foods" : foods })

def Food_Specific(request):

    context = {}
    three_foods = None

    if request.method == 'GET':
        id = request.GET.get("food_id")
        if id:
            id = int(id)
            food = Food.objects.get(pk=id)
            context['food'] = food
            three_foods = Food.objects.filter(category=food.category)[:3:]
            context['related_foods'] = three_foods


            

    return render(request , 'food.html' , context)


