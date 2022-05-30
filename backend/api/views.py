
#from django.http import JsonResponse
import json
from .models import *
from .serializers import PrinterProducerSerializer
from django.forms.models import model_to_dict


from rest_framework.decorators import api_view
from rest_framework.response import Response



# def api_home(request, *args, **kwargs):
#     data = {}

#     data = json.loads(request.body)
    
#     data['headers']=request.headers
#     data['content-type']= request.content_type
#     data['params']=dict(request.GET)
#     print(data)
    
#     return JsonResponse({"message":'Hi petuh',})

def api_create_printer_producer(request, *args, **kwargs):
    if request.GET:
        title= request.GET['title']
        printer = PrinterProducer.objects.create(title=title)
        
    #return JsonResponse({'data':'OK'})
    
# def api_home(request, *args, **kwargs):
#     model_data = PrinterProducer.objects.all().order_by('?').first()
#     data={}
#     if model_data:
        # data['id'] = model_data.pk
        # data['title'] = model_data.title
        #data = model_to_dict(model_data,fields=['id','title'])
    #return JsonResponse(data)

@api_view(['GET','POST'])
def api_home(request):
    '''
    DRF API View
    
    '''
    # if request.method != 'POST':
    #     return Response({'message':'Its fckng GET'}, status=405)

    instance= PrinterProducer.objects.all().order_by('?').first()
    data={}
    if instance:
        data = PrinterProducerSerializer(instance).data

    return Response({'message':'This is DRF motherfaka', 'data':data})