from django.db import models

class Farmer(models.Model):
    farmer_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=50)    
    bank = models.CharField(max_length=50)
    bank_account = models.CharField(max_length=50)

    def __str__(self):
        return self.farmer_name

class Farm(models.Model):
    farmer_name = models.ForeignKey('Farmer', on_delete=models.CASCADE)
    farm_name = models.CharField(max_length=50)
    farm_location = models.CharField(max_length=100)

    def __str__(self):
        return self.farm_name

class PickUp(models.Model):
    STATUS = [
        ('PENDING', 'PENDING'),
        ('COMPLETE', 'COMPLETE'),
        ('FAILED', 'FAILED'),
        ('CANCELLED', 'CANCELLED'),
    ]

    farm = models.ForeignKey('Farm', on_delete=models.CASCADE)
    fish = models.CharField(max_length=50)
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS, default='PENDING')

    def __str__(self):
        return self.farm.farm_name

class Payments(models.Model):
    pass