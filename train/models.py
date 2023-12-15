from django.db import models

class Station(models.Model):
    name=models.CharField(max_length=200)
    no=models.CharField(max_length=10)
    city=models.CharField(max_length=200)
    adress=models.TextField()
    phone_number=models.CharField(max_length=11)
    open_time=models.TimeField()
    close_time=models.TimeField()


class Train(models.Model):
    origin=models.ForeignKey(Station,on_delete=models.CASCADE)
    destination=models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    code=models.CharField(max_length=10)
    seats_number=models.IntegerField(verbose_name="capacity")
    price=models.FloatField(help_text='price in Rial')

    def __str__(self) -> str:
        return "{},{}" .format(self.name,self.code)
