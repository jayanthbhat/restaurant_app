from django.db import models

# Create your models here.
class FoodCategory(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return self.name


class FoodAttribute(models.Model):
    category = models.ForeignKey(FoodCategory,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return self.name



class FoodItems(models.Model):
    category = models.ForeignKey(FoodCategory,on_delete=models.CASCADE,null=True,blank=True)
    attributes = models.ForeignKey(FoodAttribute,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=20,null=True,blank=True)
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.name


    