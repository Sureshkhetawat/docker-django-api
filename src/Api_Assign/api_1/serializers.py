from rest_framework import serializers

class IdSerializer(serializers.Serializer):
    invalid_trigger = serializers.CharField(max_length = 100,required = True, allow_null = False)
    key = serializers.CharField(max_length = 100, required=True)
    name = serializers.CharField(max_length = 100,required=True)
    reuse = serializers.BooleanField(default=True,required=False)
    support_multiple = serializers.BooleanField(default=True,required=False)
    pick_first = serializers.BooleanField(default=False,required=False)
    supported_values = serializers.ListField(required=True)
    type = serializers.ListField(required=True)
    validation_parser = serializers.CharField(max_length=100,required=False)
    values = serializers.ListField(required=False)