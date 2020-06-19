from rest_framework import permissions
from rest_framework import viewsets

from apps.users.permissions import IsOwnerOrReadOnly
from .models import Score
from .serializers import ScoreSerializer


class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
