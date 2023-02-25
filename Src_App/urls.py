from django.urls import path
from . import views


urlpatterns = [
    path("" , views.Home , name="home"),
    path("food/" , views.Food_Specific, name='food'),
    path("foods/"  , views.Ajax_Data , name='ajax' ),
    path("search_for/" , views.Search , name='search')
]


