from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()





class Subscription(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    payment = models.BooleanField(default=False)
    plan = models.CharField(max_length=50 , choices=(('free','free'),('basic' , 'basic'),('premium','premium')))
    requests_per_day = models.IntegerField(default=0)






