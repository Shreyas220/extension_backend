from django.shortcuts import render 
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TimespentSerializer
from .models import timespent
@api_view(['POST'])
def postDetail(request):
    serializer = TimespentSerializer(data=request.data)
    if(serializer.is_valid):
        serializer.save

    return Response(serializer.data)

@api_view(['GET'])
def getAllDetail(request):
    timeData = timespent.objects.all()
    serializer = TimespentSerializer(timeData, many = True )
    return Response(serializer.data)
    
    

