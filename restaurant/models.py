from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    noOfGuests = models.IntegerField(max_length=6)
    bookingDate = models.DateTimeField()

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField()
    inventory = models.IntegerField(max_length=5)