from django.shortcuts import render
from .models import Movie
import json
from django.core.serializers import serialize

from django.http import HttpResponse
def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()

    # Serialize to a JSON
    serialized_data = serialize("json", movies)
    print(type(serialized_data)) 
    print(serialized_data)    
    
    #Set this as a variable
    return render(request, 'home.html',{'searchTerm':searchTerm, 'movies': movies,'serialized_data':serialized_data})
    
def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})