from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Users, SocialMedia, Analytics
from . serializers import UsersSerializer, SocialMediaSerializer, AnalyticsSerializer



@api_view(['POST'])
def create(request):
    serializer=UsersSerializer(data=request.data)

    if(serializer.is_valid()):
        serializer.save()

    return Response(serializer.data)



@api_view(['GET'])
def read(request):
    data = Users.objects.all()
    serializer = UsersSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def update(request, pk):
    data= Users.objects.get(id=pk)
    serializer=UsersSerializer(instance = data, data=request.data)

    if(serializer.is_valid()):
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request, pk):
    data= Users.objects.get(id=pk)
    data.delete()

    return HttpResponse('deleted')




