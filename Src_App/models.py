from django.db import models







class Food_Categorie(models.Model):

    category_name = models.CharField(max_length=50)


    def __str__(self):

        return self.category_name


class Food(models.Model):

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products' , default="" , null=False )
    category = models.ForeignKey(Food_Categorie , on_delete=models.CASCADE)
    price_previous = models.IntegerField(default=0)
    price_now = models.IntegerField(default=0)
    orders = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name





class Restaurant(models.Model):

    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="restaurants" , default="" , null=False )
    desc = models.TextField()
    menu = models.ManyToManyField(Food)
    home_delivery = models.BooleanField(default=False , null=False)
    

    def __str__(self):

        return self.name




