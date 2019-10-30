from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from dinosaur.models import Dinosaur
from dinosaur.serializers import DinosaurSerializer


@csrf_exempt
def dinosaur_list(request):
  if request.method == 'GET':
    dinosaurs = Dinosaur.objects.all()
    serializer = DinosaurSerializer(dinosaurs, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def dinosaur_detail(request, pk):
    try:
      dinosaur = Dinosaur.objects.get(pk=pk)
    except Dinosaur.DoesNotExist:
      return HttpResponse(status=404)

    if request.method == 'GET':
      serializer = DinosaurSerializer(dinosaur)
      return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
      data = JSONParser().parse(request)
      serializer = DinosaurSerializer(dinosaur, data=data)
      if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
      return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
      dinosaur.delete()
      return HttpResponse(status=204)

