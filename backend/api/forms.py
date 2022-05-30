
from django import forms

from .models import *

class PrinterProducerForm(forms.ModelForm):
    class Meta:
        model = PrinterProducer
        fields = [
            'title'
        ]