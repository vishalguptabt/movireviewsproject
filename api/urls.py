from django.urls import path
from . import views

urlpatterns = [
    path('clients',views.Clients.as_view()),
    path('clients/<int:pk>',views.ClientByPk.as_view()),
]