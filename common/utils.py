from rest_framework import serializers

def validate_unique(model,field_name,value):
    if model.objects.filter(**{f"{field_name}__iexact":value}).exists():
        raise serializers.ValidationError(f"{value} already exists.")
    return value