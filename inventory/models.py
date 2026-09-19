from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    description=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="Categories"

class Item(models.Model):
    sku=models.CharField(max_length=12,unique=True,db_index=True)
    name=models.CharField(max_length=100)
    quantity_on_hand=models.PositiveIntegerField()
    unit_price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="items")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} x {self.category}"