from django.contrib import admin 
from django.urls import path 
  
# importing views from views..py 
from . import views
  
urlpatterns = [ 
    path('',  views.index, name="index"),
    path('generate', views.generate, name="generate"),
    path('generate', views.generate_pdf, name="generate_pdf"),
]