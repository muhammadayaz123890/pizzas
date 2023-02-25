from django.urls import path
from . import views


urlpatterns = [
    path("" , views.Home , name="home"),
    path("food" , views.Food, name='food'),
    path("foods/"  , views.Ajax_Data , name='ajax' )
]


