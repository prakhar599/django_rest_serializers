import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSeralizer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def stucreate(request):
    if request.method=="POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pydata = JSONParser().parse(stream)
        serializer = StudentSeralizer(data=pydata)
        if serializer.is_valid():
            serializer.save()
            res = {'message':'Data has been inserted in DB'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')   
        
