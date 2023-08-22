from rest_framework import  generics
from .serializers import ClientSeializer
from client.models import Client

class Clients(generics.ListAPIView):
    serializer_class=ClientSeializer
    ##TODO Add Permissions Check
    
    def get_queryset(self):
        return Client.objects.all()

class ClientByPk(generics.RetrieveAPIView):
    serializer_class=ClientSeializer
    ##TODO Add Permissions Check
    
    def get_queryset(self):
        a_pk = self.kwargs.get("pk")
        return Client.objects.filter(pk=a_pk)

# Create your views here.
