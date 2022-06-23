
from pyexpat import model
from rest_framework import serializers

from .models import *

class RepairCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=RepairCompany
        fields='all'


class FactorySerializer(serializers.ModelSerializer):
    my_example=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Factory
        fields = [
            'title',
            'email',
            'my_example'
        ]
    def get_my_example(self, obj):
        try:
            return obj.get_example()
        except:
            return None


class PrinterProducerSerializer(serializers.ModelSerializer):
    my_example=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = PrinterProducer
        fields = [
            'title',
            'my_example'#указываем значение ключа словаря, а в значении будет результат метода
        ]
    def get_my_example(self, obj):
        return obj.get_example()




class PrinterModelSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=PrinterModelSeries
        fields = '__all__'


class FactoryPrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryPrinter
        fields = ['id','hostname','place', 'model_series','factory','get_absolute_url','model',]


class CartrigeSerializer(serializers.ModelSerializer):
    # model_series = serializers.SerializerMethodField(read_only=True)
    
    
    class Meta:
        model= Cartrige
        fields = ['id','title','quantity','min_quantity','alert_quantity','model_series','updated','get_model_series','get_absolute_url']
    
    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)

    # def get_model_series(self,obj):
    #     try:
    #         model_series=PrinterModelSeries.objects.filter(id=obj.model_series.id)

    #         return PrinterModelSeriesSerializer(model_series).data
    #     except:
    #         return None