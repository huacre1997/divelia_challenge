from rest_framework import generics
from apps.toys.models import Toy, Gift
from .serializers import ToySerializer, GiftSerializer
from rest_framework import permissions, authentication


class ToyListView(generics.ListCreateAPIView):
    queryset = Toy.objects.filter(is_active=True)
    serializer_class = ToySerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = Toy.objects.filter(owner=user, is_active=True)
        return qs


class ToyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Toy.objects.filter(is_active=True)
    serializer_class = ToySerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class GiftCreateView(generics.CreateAPIView):
    serializer_class = GiftSerializer
    queryset = Gift.objects.filter(is_active=True)
