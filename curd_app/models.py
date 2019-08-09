from django.db import models

class Product_Data(models.Model):
    P_id = models.IntegerField()
    P_name = models.CharField(max_length=100)
    P_cost = models.IntegerField()
    P_color = models.CharField(max_length=50)
    P_class = models.CharField(max_length=50)
