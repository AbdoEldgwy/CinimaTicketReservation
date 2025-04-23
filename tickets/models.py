from django.db import models

# Guest -- Moive -- reservations 
class Guest(models.Model):
    Name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)

class Movie(models.Model):
    Hall = models.CharField(max_length=20)
    Movie_Name = models.CharField(max_length=50)
    Show_Time = models.DateTimeField()
    Price = models.IntegerField()

class Reservation(models.Model):
    Guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='reservations')
    Movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reservations')
    Seat_Number = models.CharField(max_length=10)