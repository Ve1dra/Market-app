from rest_framework.permissions import BasePermission

class RiderPermission(BasePermission):
    message = "You need to be a Rider before you can do this"
    def has_permission(self, request, view):
        user = request.user.role == "RIDER"
        return user
class SellerPermission(BasePermission):
    message = "You need to be a Seller before you can do this"
    def has_permission(self, request, view):
        return request.user.role == "SELLER"
class BuyerRiderPermission(BasePermission):
    message = "You need to be a Buyer/Rider before you can do this"
    def has_permission(self, request, view):
        return request.user.role in ["RIDER", "BUYER"]