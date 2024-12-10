from django.shortcuts import render
from rest_framework.decorators import api_view
from tickets.models import Guest,Movie,Reservation
from rest_framework.response import Response
#from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
#from django.http.response import Response
from .serializers import GuestSerializer, MoviesSerializer, ReservationsSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

#from import requests


#Get POST
@api_view(['GET','POST'])
def FBV_List(request):
    #GET
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)        
        return Response(serializer.data)
    #POST
    elif request.method == 'POST':
        serializer = GuestSerializer(data=request.data)        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


#Get PUT 
@api_view(['GET', 'PUT','DELETE'])
def FBV_one(request,pk):
    #GET
    if request.method == 'GET':
        guest = Guest.objects.get(pk=pk)        
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    #PUT
    elif request.method == 'PUT':
        guest = Guest.objects.get(pk=pk)
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    #DELETE
    elif request.method == 'DELETE':
        guest = Guest.objects.get(pk=pk)
        guest.delete()
        return Response(status=204)
    
    
class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = [IsAuthenticated]
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationsSerializer
    
