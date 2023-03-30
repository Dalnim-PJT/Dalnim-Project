from django.urls import path
from . import views

app_name = 'infobases'
urlpatterns = [
    path('', views.main, name='main'),
    
]
