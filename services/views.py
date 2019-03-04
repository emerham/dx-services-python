from rest_framework import viewsets, permissions

from services.models import (
    Services,
    Categories,
    Synonyms,
    EntityQueue,
    EntityQueueItem,
)
from services.serializers import (
    ServiceSerializer,
    CategorySerializer,
    SynonymSerializer,
    EntityQueueSerializer,
    EntityQueueItemSerializer,
)


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all().order_by('id')
    serializer_class = ServiceSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )


class SynonymViewSet(viewsets.ModelViewSet):
    queryset = Synonyms.objects.all().order_by('name')
    serializer_class = SynonymSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )


class EntityQueueItemViewSet(viewsets.ModelViewSet):
    queryset = EntityQueueItem.objects.all()
    serializer_class = EntityQueueItemSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )


class EntityQueueViewSet(viewsets.ModelViewSet):
    queryset = EntityQueue.objects.all()
    serializer_class = EntityQueueSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
