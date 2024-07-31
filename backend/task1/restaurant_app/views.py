from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Restaurant
from .serializers import RestaurantSerializer

class RestaurantListCreate(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
