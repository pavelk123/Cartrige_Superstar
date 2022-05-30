from rest_framework import serializers

from .models import *

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