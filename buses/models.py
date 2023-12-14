from django.db import models


class Terminal(models.Model):
    name=models.CharField(max_length=200)
    no=models.CharField(max_length=10)
    city=models.CharField(max_length=300)
    adress=models.TextField()
    phone_number=models.CharField(max_length=11)
    open_time=models.TimeField()
    close_time=models.TimeField()


class Bus(models.Model):
    origin=models.ForeignKey(Terminal,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    type=models.CharField(max_length=100)
    no=models.CharField(max_length=10)
    capacity=models.IntegerField()
    price=models.FloatField()


