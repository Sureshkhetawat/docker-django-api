from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

from .serializers import AgeSerializer
from .AgeSlotValidation import validate_numeric_entity

class ageValidationAPIView(APIView):

    def get(self, request):
        return Response("Hello World, This is age validation GET request")

    def post(self, request):
        data = request.data
        serializer = AgeSerializer(data = data)

        if serializer.is_valid():
            data = serializer.data
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        values = data['values']
        constraint = data['constraint']
        invalid_trigger = data['invalid_trigger']+"_stated"
        key = data['key']
        var_name = data['var_name']
        pick_first = data['pick_first']
        support_multiple = data['support_multiple']

        try:
            result = validate_numeric_entity(values, invalid_trigger, key,support_multiple, pick_first, constraint, var_name)
        except Exception as error:
            print(error)
            return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)

        result_key = ["filled", "partially_filled", "trigger","parameters"]
        result = dict(zip(result_key,result))

        return Response(result)