from rest_framework import serializers
from tickets.models import Guest,Movie,Reservation

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'
        
class ReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields='__all__'
        
class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Guest
        fields=['pk','reservation','name','mobile']