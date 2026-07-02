from django.shortcuts import render
from API.models import Player
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from API.serializers import Playerserializer
# Create your views here.
def home(request):
    