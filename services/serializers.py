from rest_framework import serializers

from services.models import Categories, Services, Synonyms, EntityQueue, EntityQueueItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class SynonymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Synonyms
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    """
    To render the relationships by their name field rather than by their id
    we use a SlugRelatedField
    """
    field_service_synonyms = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Synonyms.objects.all(),
        many=True,
        allow_null=True)
    field_service_category = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Categories.objects.all(),
        many=True,
        allow_null=True)

    class Meta:
        model = Services
        fields = '__all__'


class EntityQueueItemSerializer(serializers.ModelSerializer):
    service = serializers.SlugRelatedField(
        slug_field='title',
        queryset=Services.objects.all())
    queue = serializers.SlugRelatedField(
        slug_field='title',
        queryset=EntityQueue.objects.all())

    class Meta:
        model = EntityQueueItem
        fields = '__all__'


class EntityQueueSerializer(serializers.ModelSerializer):

    class Meta:
        model = EntityQueue
        fields = ('created_at', 'modified_at', 'title')
