from rest_framework import serializers
from client.models import Client

class ClientSeializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields=['id','first_name','last_name','company_name']
