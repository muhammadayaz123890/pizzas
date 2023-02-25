from django.contrib import admin
from .models import Subscription



class Sub_Admin(admin.ModelAdmin):

    list_display = ['user', 'key' , 'plan']

admin.site.register(Subscription, Sub_Admin)





