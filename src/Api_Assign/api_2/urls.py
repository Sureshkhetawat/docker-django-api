from django.urls import path
from .views import ageValidationAPIView

urlpatterns = [
    path("AgeValidation/",ageValidationAPIView.as_view(), name = "AgeValidation")
]
