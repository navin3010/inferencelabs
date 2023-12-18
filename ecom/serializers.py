from ecom import models
from rest_framework import serializers

# class CategorySerializer(serializers.ModelSerializer):
#     category_id  = serializers.ReadOnlyField(source = "id")

#     class Meta:
#         model = models.Categories
#         fields = ["category_id", "title"]

class WriteCategorySerializer(serializers.ModelSerializer):
    category_id  = serializers.ReadOnlyField(source = "id")

    class Meta:
        model = models.Categories
        fields = ["category_id", "title"]

class ProductsSerializer(serializers.ModelSerializer):
    product_id = serializers.ReadOnlyField(source = "id")
    category = WriteCategorySerializer()

    class Meta:
        model = models.Products
        fields = ["product_id", "title", "description", "price", "category", "is_active"]

# class WriteReviewSerializer(serializers.ModelSerializer):
#     print("Serializer")
#     review_id = serializers.ReadOnlyField(source = "id")
#     product = ProductsSerializer()

#     class Meta:
#         model = models.Review
#         fields = ["review_id", "product", "rating", "pros", "review"]