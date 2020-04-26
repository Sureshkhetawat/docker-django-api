from django.shortcuts import render
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import IdSerializer
from .IdSlotValidation import validate_finite_values_entity

# Create your views here.

class idValidationAPIView(APIView):

    def get(self, request):
        return Response("Hello world")

    def post(self, request):
        data = request.data
        serializer = IdSerializer(data = data)

        if serializer.is_valid():
            data = serializer.data
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        values = data['values']
        supported_values = data['supported_values']
        invalid_trigger = data['invalid_trigger']
        key = data['key']
        support_multiple = data['support_multiple']
        pick_first = data['pick_first']

        try:
            result = validate_finite_values_entity(values,supported_values,invalid_trigger,key,support_multiple,pick_first)
        except Exception as error:
            print(error)
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


        result_key = ["filled", "partially_filled", "trigger","parameters"]

        result = dict(zip(result_key,result))
        return Response(result)
