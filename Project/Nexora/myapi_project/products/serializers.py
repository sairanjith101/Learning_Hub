from rest_framework import serializers
from .models import Category, Brand, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source="category", write_only=True)
    brand_id = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all(), source="brand", write_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'stock',
                  'category', 'brand', 'category_id', 'brand_id',
                  'seller', 'created_at', 'updated_at')
        read_only_fields = ('id', 'seller', 'created_at', 'updated_at')
