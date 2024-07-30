from django.contrib import admin
from django.urls import path

# Importing views from views.py
from . import views
from .views import GeneratePdf  # Ensure the GeneratePdf class is imported

urlpatterns = [
    path('', views.index, name="index"),
    path('generate', views.generate, name="generate"),
    path('GeneratePdf/', GeneratePdf.as_view(), name="GeneratePdf"),  # Added trailing slash and corrected usage
]
