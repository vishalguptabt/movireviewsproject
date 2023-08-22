from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    #description = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250)


    def __str__(self):
        return self.first_name +' '+self.last_name