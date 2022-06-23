
#from django.http import JsonResponse

import json

from yaml import serialize



from .models import *
from .serializers import *
from django.forms.models import model_to_dict

from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView,UpdateAPIView
from rest_framework.views import APIView
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



    # instance= Factory.objects.all().order_by('?').first()
    # data={}
    # if instance:
    #     data = PrinterProducerSerializer(instance).data

    # return Response({'message':'This is DRF motherfaka', 'data':data})
    data = request.data
    serializer=FactorySerializer(data=data)
    if serializer.is_valid():
        
        instance= serializer.save()
        data= serializer.data
        print(instance)
        return Response(data)

#######################################################################

# @api_view(['GET'])
# def all_cartriges(request):
    
#     model_data = Cartrige.objects.all()
#     if model_data:
        
#         data = CartrigeSerializer(model_data,many=True).data
    
#     return Response({'cartriges':data} if data else {'message':'тут ничего нет'})

# class CartrigeAPIList(ListCreateAPIView):
#     queryset = Cartrige.objects.all()
#     serializer_class = CartrigeSerializer


# class CartrigeAPIUpdate(UpdateAPIView):
#     queryset = Cartrige.objects.all()
#     serializer_class = CartrigeSerializer


# class CartrigeAPIView(APIView):
#     def get(self,request,id):
#         try:
#             model_data = Cartrige.objects.get(pk=id)
#             data = CartrigeSerializer(model_data).data
#             return Response({'cartrige':data})
#         except:
#             return Response({'status':'Таких куртруджей нету'})

#     def put(self,request, *args, **kwargs):
#         pk = kwargs.get('id',None)
#         if pk:
#             try:
#                 cartrige = Cartrige.objects.get(pk = pk)
#             except:
#                 return Response({'status':'Таких куртруджей нету'})                
#             serializer=CartrigeSerializer(data=request.data, instance=cartrige)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response({'changes':serializer.data})

#     def delete(self,request, *args, **kwargs):
#         pk = kwargs.get('id',None)
#         if pk:
#             try:
#                 cartrige = Cartrige.objects.get(pk = pk)
#             except:
#                 return Response({'status':'Таких куртруджей нету'}) 
#             cartrige.delete()
#             return Response({'status':'Куртрудж удален'})


class RepairCompanyViewSet(viewsets.ModelViewSet):
    queryset= RepairCompany.objects.all()
    serializer_class = RepairCompanySerializer


class FactoryViewSet(viewsets.ModelViewSet):
    queryset=Factory.objects.all()
    serializer_class= FactorySerializer

class PrinterProducerViewSet(viewsets.ModelViewSet):
    queryset=PrinterProducer.objects.all()
    serializer_class=PrinterProducerSerializer


class PrinterModelSeriesViewSet(viewsets.ModelViewSet):
    queryset=PrinterModelSeries.objects.all()
    serializer_class= PrinterModelSeriesSerializer


class FactoryPrinterViewSet(viewsets.ModelViewSet):
    queryset= FactoryPrinter.objects.all()
    serializer_class=FactoryPrinterSerializer


class CartrigeViewSet(viewsets.ModelViewSet):
    queryset=Cartrige.objects.all()
    serializer_class = CartrigeSerializer

    # def get_queryset(self):
    #     return self.queryset[:2]


    # @action(methods=['get'],detail=True)
    # def model_series(self,request,pk=None):
    #     # models = PrinterModelSeries.objects.all()
    #     # return Response({'models':[m.title for m in models]})
    #     model = PrinterModelSeries.objects.get()
    #     return Response({'model':model.title})

    @action(methods=['get'],detail=True)
    def factory_printers(self, request,pk):
        cartrige = Cartrige.objects.get(pk=pk)
        model=PrinterModelSeries.objects.get(pk =cartrige.model_series.pk)
        #factory_printers=FactoryPrinter.objects.filter(model_series = model)
        factory_printers=model.factoryprinter_set.all()
        
        serializer= FactoryPrinterSerializer(factory_printers,many=True)
        print(serializer.data)
        return Response(serializer.data)
    

