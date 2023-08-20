from django.db import models

# Create your models here.
class StoreData(models.Model):
    lstat = models.FloatField()
    rm = models.FloatField()
    ptratio = models.FloatField()
    prediction = models.FloatField()