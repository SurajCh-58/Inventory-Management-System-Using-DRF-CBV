from django.urls import path,include
from rest_framework.routers import DefaultRouter
from inventory.views import CategoryView,ItemView

router=DefaultRouter()
router.register(r'category',CategoryView,basename="category")
router.register(r'items',ItemView,basename="items")

urlpatterns = [
    path('',include(router.urls))
]
