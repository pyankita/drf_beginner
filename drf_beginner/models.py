from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.charField(max_length=100,null=True,blank=True)
    price=models.FloatField(null=True,blank=True)

    def __str__(self):
        self.name