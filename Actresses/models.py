from django.db import models

# Create your models here.
class Actres(models.Model):
    actres_name=models.CharField(max_length=36)
    actres_img=models.ImageField(upload_to='static/images/actress')
    actres_sum=models.CharField(max_length=1600)

    def __str__(self):
        return "Name : " + self.actres_name


class ActresD(models.Model):
    actres_id=models.ForeignKey(Actres,on_delete=models.CASCADE)
    date_of_birth=models.DateField(max_length=36,null=True,blank=True)
    nick_name=models.CharField(max_length=36,null=True,blank=True)
    marital_status=models.CharField(max_length=36,null=True,blank=True)
    affairs=models.CharField(max_length=36,null=True,blank=True)
    birthplace_place=models.CharField(max_length=100,null=True,blank=True)
    ethnicity=models.CharField(max_length=36,null=True,blank=True)
    nationality=models.CharField(max_length=36,null=True,blank=True)
    eye_color=models.CharField(max_length=36,null=True,blank=True)
    hair_color=models.CharField(max_length=36,null=True,blank=True)
    height=models.CharField(max_length=36,null=True,blank=True)
    weight=models.CharField(max_length=36,null=True,blank=True)
    education=models.CharField(max_length=106,null=True,blank=True)
    horoscope=models.CharField(max_length=36,null=True,blank=True)
    net_worth=models.CharField(max_length=36,null=True,blank=True)
    about_career=models.CharField(max_length=1600,null=True,blank=True)

    def __str__(self):
        return "Name : " + self.nick_name