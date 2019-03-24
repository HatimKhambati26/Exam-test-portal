from django.urls import path,include
from . import views
urlpatterns = [
    
    path('', views.details),
    path('IOT/', views.iot),
    path('Ethical Hacking/', views.eh),
    path('Augmented Reality/', views.ar),
    path('Machine Learning/', views.ml),
]
