
import email
from pyexpat import model
from turtle import title
from django.db import models

class Factory(models.Model):
    title = models.CharField(max_length=120)
    email = models.EmailField() 


class PrinterProducer(models.Model):
    title = models.CharField(max_length=120)


class PrinterModelSeries(models.Model):
    title = models.CharField(max_length=254)
    
    producer=models.ForeignKey(PrinterProducer, on_delete=models.CASCADE)


class FactoryPrinter(models.Model):
    hostname = models.CharField(max_length=120)
    model = models.CharField(max_length=120)
    place= models.TextField(blank=True)
    model_series = models.ForeignKey(PrinterModelSeries, on_delete=models.CASCADE)
    factory= models.ForeignKey(Factory, on_delete=models.CASCADE)


class Cartrige(models.Model):
    title= models.CharField(max_length=120)
    quantity = models.IntegerField()
    model_series= models.ForeignKey(PrinterModelSeries, on_delete=models.CASCADE)
