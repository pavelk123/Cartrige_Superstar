from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    # data = {}

    # data = json.loads(request.body)
    
    # data['headers']=request.headers
    # data['content-type']= request.content_type
    # data['params']=dict(request.GET)
    # print(data)
    
    return JsonResponse({"message":'Hi petuh',})