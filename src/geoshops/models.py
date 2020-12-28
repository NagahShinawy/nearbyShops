from django.contrib.gis.db import models

# Create your models here.


class Shop(models.Model):
    name = models.CharField(max_length=200)
    location = models.PointField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    # objects = models.manager

    def __str__(self):
        return f'{self.city}-{self.address}-{self.name}'