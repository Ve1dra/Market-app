from django.urls import path
from product.views import ProductView, SingleProduct

urlpatterns = [
    path('products/', ProductView.as_view()),
    path('products/<uuid:id>', SingleProduct.as_view())
]