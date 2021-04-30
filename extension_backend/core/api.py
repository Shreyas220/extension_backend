from django.shortcuts import render 
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TimespentSerializer
from .models import timespent
from rest_framework import status
import json



@api_view(['POST'])
def postDetail(request):
    request_data = json.loads(request.body)

    try:
        #check if the site exists 
        site = timespent.objects.get(url=request_data['url'])


    except site.DoesNotExist:
        postDetailNew(request.body)

    else:
        postDetailAdd(request.body)



def postDetailAdd(data_site):
    request_data = json.loads(request.body)
    site = timespent.objects.get(url=request_data['url'])
    request_data['timepassed'] =  request_data['timepassed'] + site['timepassed'] 

    serializer = TimespentSerializer(site, data=request_data)



def postDetailNew(data_site):
    serializer = TimespentSerializer(data=data_site)
    try:
        serializer.is_valid(raise_exception=True)

    except:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


    

@api_view(['GET'])
def getAllDetail(request):
    timeData = timespent.objects.all()
    serializer = TimespentSerializer(timeData, many = True )
    return Response(serializer.data, status=status.HTTP_200_OK)
    


