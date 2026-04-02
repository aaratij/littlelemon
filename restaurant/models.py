from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    noOfGuests = models.IntegerField()
    bookingDate = models.DateTimeField()

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=4, max_digits=8)
    inventory = models.IntegerField()
    def __str__(self):
        return f'{self.title} : {str(self.price)}'