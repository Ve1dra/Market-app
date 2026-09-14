from rest_framework import serializers
from .models import Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ["id", "owner", "name", "category"
                  , "price", "description", "quantity", "image"
                  , "created_at", "updated_at", "quantity_sold"]
        read_only_fields = ["created_at", "updated_at"
                            , "quanttity_sold", "id", "owner"]