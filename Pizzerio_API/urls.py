from django.urls import path
from . import views



urlpatterns = [
    path("developer_console/" , views.Developer_Console_Home , name='api_console'),
    path("api_subscribe/" , views.Subscribe , name='api_subscribe'),
    path("sub_now/" , views.Subscribe_to_plan , name='add_subscription'),
    path('get_data/' , views.Get_Data , name="get_data")
]






