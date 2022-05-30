
from django.db import models

class RepairCompany(models.Model):
    title = models.CharField(max_length=120)
    email = models.EmailField()
    

class Factory(models.Model):
    title = models.CharField(max_length=120)
    email = models.EmailField() 


class PrinterProducer(models.Model):
    title = models.CharField(max_length=120)
    repair_company=models.ForeignKey(RepairCompany,on_delete=models.CASCADE)

    def get_example(self):
        return 'example'

    def __str__(self):
        return self.title

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
    min_quantity  = models.IntegerField()
    alert_quantity = models.BooleanField(default=False)
    model_series= models.ForeignKey(PrinterModelSeries, on_delete=models.CASCADE)
    
    
    def save(self, *args, **kwargs):
        if self.quantity < 0:
            self.quantity = 0
        if self.quantity < self.min_quantity:
            self.alert_quantity = True
        elif self.quantity >= self.min_quantity:
            self.alert_quantity=False
        super(Cartrige, self).save(*args, **kwargs)

