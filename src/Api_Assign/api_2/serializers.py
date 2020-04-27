from rest_framework import serializers

class AgeSerializer(serializers.Serializer):
    invalid_trigger = serializers.CharField(max_length = 100,required = True)
    key = serializers.CharField(max_length = 100, required=True)
    name = serializers.CharField(max_length = 100,required=True)
    reuse = serializers.BooleanField(default=True,required=False)
    support_multiple = serializers.BooleanField(default=False,required=False)
    pick_first = serializers.BooleanField(default=True,required=False)
    type = serializers.ListField(required=True)
    validation_parser = serializers.CharField(max_length=100,required=False)
    constraint = serializers.CharField(max_length = 100,required=True)
    var_name = serializers.CharField(required = True)
    values = serializers.ListField(required=False)