from django.db import models

class PickUp(models.Model):
    farm = models.CharField(max_length=50)
    fish = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return self.farm