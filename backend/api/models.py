
from django.db import models

class RepairCompany(models.Model):
    title = models.CharField(max_length=120)
    email = models.EmailField()
    

class Factory(models.Model):
    title = models.CharField(max_length=120)
    email = models.EmailField() 

    def get_example(self):
        return 'example'


class PrinterProducer(models.Model):
    title = models.CharField(max_length=120, unique=True)
    repair_company=models.ForeignKey(RepairCompany,on_delete=models.CASCADE)

    def get_example(self):
        return 'example'

    def __str__(self):
        return self.title

class PrinterModelSeries(models.Model):
    title = models.CharField(max_length=254)
    

    producer=models.ForeignKey(PrinterProducer, on_delete=models.CASCADE)


    def __str__(self):
        return self.title



class FactoryPrinter(models.Model):
    hostname = models.CharField(max_length=120)
    model = models.CharField(max_length=120)
    place= models.TextField(blank=True)
    model_series = models.ForeignKey(PrinterModelSeries, on_delete=models.CASCADE)
    factory= models.ForeignKey(Factory, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return f'/printers/{self.id}/'


class Cartrige(models.Model):
    title= models.CharField(max_length=120)
    quantity = models.IntegerField()
    min_quantity  = models.IntegerField()
    alert_quantity = models.BooleanField(default=False)
    model_series= models.ForeignKey(PrinterModelSeries, on_delete=models.CASCADE, blank=True)
    updated = models.DateTimeField(auto_now=True, )
    
    
    class Meta:
        ordering = ('-updated',)


    
    def save(self, *args, **kwargs):
        if self.quantity < 0:
            self.quantity = 0
        if self.quantity < self.min_quantity:
            self.alert_quantity = True
        elif self.quantity >= self.min_quantity:
            self.alert_quantity=False
        super(Cartrige, self).save(*args, **kwargs)

    
    def get_model_series(self):
        model =PrinterModelSeries.objects.get(pk=self.model_series.pk)
        return model.title
    # def model_series_show(self):
    #     return PrinterModelSeriesSerializer(PrinterModelSeries.objects.get(pk=self.model_series.pk))
    
    
    def get_absolute_url(self):
        return f'/cartriges/{self.id}/'















#c = Cartrige.objects.get(pk=3)
# ms=PrinterModelSeries.objects.get(pk=1)
# f= Factory.objects.get(pk=2) 
#  fp = FactoryPrinter(factory=f,model_series=ms, hostname='PPET-00016',model='HP LaserJet Pro M527c',place='Двор>Лавка>Слева')
#p = PrinterProducer.objects.get(pk=1) 
# ms=PrinterModelSeries(title='HI BLACK HP LJ Enterprise M602 series /M603 series / M4555 series',producer=p)
 #c= Cartrige(title='Cactus CS-CE390XS',quantity=7,min_quantity=4,model_series=ms)