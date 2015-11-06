from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    json_data = {'gpi1': 'HIGH'}
    return HttpResponse("is this working")
