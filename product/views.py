from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.response import Response
from product.models import Products
from product.serializers import ProductSerializer
from utils.pagination import CustomPagination
from drf_yasg import openapi
from django.db.models import Q
from drf_yasg.utils   import swagger_auto_schema

# Create your views here.


class ProductView(generics.GenericAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response(data=serializer.data, status=201)

    def get_queryset(self):
            search = self.request.query_params.get("search", None)
            all_products = Products.objects.all()
            if search:
                all_products = all_products.filter(Q(name__icontains=search) | Q(description__icontains=search))
            return all_products
    
    @swagger_auto_schema(
            manual_parameters=[
                openapi.Parameter(
                    "search", openapi.IN_QUERY,
                    description="Search product",
                    required=False, type=openapi.TYPE_STRING)
            ]
    )
    def get(self, request):
        all_products = self.get_queryset()
        pagination = self.paginate_queryset(all_products)
        if pagination is not None:
            serializer = self.serializer_class(all_products, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(all_products, many=True)
        return Response(data=serializer.data, status=200)

class SingleProduct(generics.GenericAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        id = self.kwargs['id']
        all_products = get_object_or_404(Products, id=id)
        return all_products
    
    def get(self, request, id):
        products = self.get_queryset()
        serializer = self.serializer_class(products)
        return Response(serializer.data, status=200)