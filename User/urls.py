from django.urls import path
from User.views import SellerView, Close
urlpatterns = [
    path('open/', SellerView.as_view()),
    path('close/', Close.as_view()),
]