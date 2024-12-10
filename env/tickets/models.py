from django.db import models

#Guest ---- Movie ----Reservation


class Movie(models.Model):
    hall=models.CharField( max_length=10)
    movie=models.CharField( max_length=10)
    date=models.DateField( auto_now=False, auto_now_add=False)


class Guest(models.Model):
    name=models.CharField( max_length=30)
    mobile=models.CharField( max_length=15)
    


class Reservation(models.Model):
    guest=models.ForeignKey(Guest,related_name='reservation' , on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie, related_name='reservation', on_delete=models.CASCADE)
    seat=models.CharField( max_length=5)
    status=models.CharField( max_length=10)
    date=models.DateField( auto_now=False, auto_now_add=False)
    time=models.TimeField()
    price=models.FloatField()
    discount=models.FloatField()
    total=models.FloatField()
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField( auto_now=True)
    cancelled_at=models.DateTimeField(null=True)
    cancelled_reason=models.CharField( max_length=255, null=True)
    cancelled_by=models.CharField( max_length=30, null=True)


