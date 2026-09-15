from rest_framework import serializers
from inventory.models import Category,Item

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=["id","name","description"]
        read_only_fields=["id"]

    def validate_name(self,name):
        if Category.objects.filter(name__iexact=name).exists():
            raise serializers.ValidationError(f"{name} already exists.")
        return name
    
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields=["id","sku","name","quantity_on_hand","unit_price","category","created_at","updated_at"]
        read_only_fields=["id","created_at","updated_at"]

    def validate_sku(self,sku):
        if Item.objects.filter(sku__iexact=sku).exists():
            raise serializers.ValidationError(f"{sku} already exists.")
        return sku
    def validate_name(self,name):
        if Item.objects.filter(name__iexact=name).exists():
            raise serializers.ValidationError(f"{name} already exists.")
        return name