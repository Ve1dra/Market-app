from rest_framework import generics, permissions
from rest_framework.response import Response

from authentication.permissions import SellerPermission


# Create your views here.
class SellerView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, SellerPermission]

    def get(self, request):
        return Response(data={"message": "Open endpoint availabe"}, status=200)


class Close(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(data={"message": "Close endpoint available"}, status=200)
