from django.contrib import admin
from django.urls import path, include
from .views import idValidationAPIView

urlpatterns = [
    path('IdValidation/',idValidationAPIView.as_view(),name = "IdValidation"),
]