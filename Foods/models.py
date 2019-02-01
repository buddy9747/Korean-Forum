from django.db import models

# Create your models here.
class dish(models.Model):
    dish_name=models.CharField(max_length=100)
    dish_img=models.ImageField(upload_to='static/images/dishes')
    dish_sum=models.CharField(max_length=1600)

    def __str__(self):
        return "Dish : "+self.dish_name

class dishD(models.Model):
    dish_id=models.ForeignKey(dish,on_delete=models.CASCADE)
    ingridient=models.CharField(max_length=1800,null=True,blank=True)
    instructions=models.CharField(max_length=18000,null=True,blank=True)
    about=models.CharField(max_length=1800,null=True,blank=True)
