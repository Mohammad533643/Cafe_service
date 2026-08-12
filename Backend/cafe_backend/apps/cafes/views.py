from rest_framework import viewsets, permissions
from .models import Cafe
from .serializers import CafeSerializers
from .permissions import IsOwnerOrReadonly


class CafeViewSet(viewsets.ModelViewSet):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializers
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadonly]

    def perform_create(self, serializer):
        serializer.save(Owner=self.request.user)
