from django.db import models

# Create your models here.
class Items(models.Model):
    name=models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity =  models.IntegerField()
    barcode = models.IntegerField()

    def __str__(self):
        return self.name