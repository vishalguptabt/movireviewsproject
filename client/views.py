from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Client
import json

def client(request):
    clients = Client.objects.all()
    return render(request, 'client.html', {'clients':clients}) 

