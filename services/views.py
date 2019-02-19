from rest_framework import viewsets, permissions

from services.models import Services
from services.models import Categories
from services.models import Synonyms
from services.serializers import ServiceSerializer
from services.serializers import CategorySerializer
from services.serializers import SynonymSerializer


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
