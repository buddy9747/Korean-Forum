from django.db import models

# Create your models here.
class Place(models.Model):
    place_name=models.CharField(max_length=136)
    place_img=models.ImageField(upload_to='static/images/places')
    place_sum=models.CharField(max_length=1600)

    def __str__(self):
        return "Place : " + self.place_name

class PlaceD(models.Model):
    place_id=models.ForeignKey(Place,on_delete=models.CASCADE)
    what_is_it=models.CharField(max_length=3600)
    why_so_famous=models.CharField(max_length=3600)