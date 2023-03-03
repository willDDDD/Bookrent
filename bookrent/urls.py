from django.urls import path
from . import views 
from bookrent.views import *

urlpatterns = [
     path('mainpage/', mainpage),
]