from rest_framework import generics
from apps.pets.models import Pet
from .serializers import PetSerializer
from rest_framework import permissions, authentication


class PetListView(generics.ListCreateAPIView):
    queryset = Pet.objects.filter(is_active=True)
    serializer_class = PetSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = Pet.objects.filter(owner=user, is_active=True)
        return qs


class PetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
