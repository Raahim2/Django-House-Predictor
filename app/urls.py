from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path("", views.predict_price , name="predict")
    
]