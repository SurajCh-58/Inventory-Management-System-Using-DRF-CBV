from inventory.models import Category,Item
from inventory.serializers import CategorySerializer,ItemSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class CategoryView(ModelViewSet):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()

class ItemView(ModelViewSet):
    serializer_class=ItemSerializer
    queryset=Item.objects.all()