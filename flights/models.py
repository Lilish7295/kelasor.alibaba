from django.db import models

class Airport(models.Model):
    name=models.CharField(max_length=200)
    no=models.CharField(max_length=10)
    city=models.CharField(max_length=200)
    adress=models.TextField()
    phone_number=models.CharField(max_length=11)
    open_time=models.TimeField()
    close_time=models.TimeField()


class Flight(models.Model):
    origin=models.ForeignKey(Airport,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    flight_number=models.CharField(max_length=10)
    seats_number=models.IntegerField()
    price=models.FloatField()

