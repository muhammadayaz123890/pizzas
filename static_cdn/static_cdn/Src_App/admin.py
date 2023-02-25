from django.contrib import admin
from .models import Food
from .models import Food_Categorie
class Food_Admin(admin.ModelAdmin):

    list_display = ['name', 'price_now']
    search_fields = ['name']
    readonly_fields = ['orders']

class Category_Admin(admin.ModelAdmin):

    list_display = ['category_name' ]


admin.site.register(Food_Categorie,Category_Admin)
admin.site.register(Food , Food_Admin)