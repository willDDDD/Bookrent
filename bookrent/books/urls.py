from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.main),
    path('rent/',views.rent),
    path('rent/result',views.result),
    path('home/',views.home),
    path('returnbooks/',views.returnbooks),
]