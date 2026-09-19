from rest_framework import serializers
from common.utils import validate_unique
from inventory.models import Category,Item

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=["id","name","description"]
        read_only_fields=["id"]

    def validate_name(self,name):
        return validate_unique(Category,"name",name)
    
class ItemSerializer(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    class Meta:
        model=Item
        fields=["id","sku","name","quantity_on_hand","unit_price","category","created_at","updated_at"]
        read_only_fields=["id","created_at","updated_at"]

    def validate_sku(self,sku):
        return validate_unique(Item,"sku",sku)
    def validate_name(self,name):
        return validate_unique(Item,"name",name)