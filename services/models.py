from django.db import models


# Create your models here.
class BaseModel(models.Model):
    """
    I hear RoR has this by default, who doesn't need these two fields!
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Categories(BaseModel):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Synonyms(models.Model):
    name = models.CharField(max_length=256, unique=True)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Services(BaseModel):
    title = models.CharField(max_length=256)
    field_service_description = models.TextField(blank=True)
    field_service_category = models.ManyToManyField(
        Categories, related_name='Categories', blank=True)
    field_service_synonyms = models.ManyToManyField(
        'Synonyms', related_name='Synonyms', blank=True)
    field_service_url = models.URLField()
    field_service_icon = models.CharField(max_length=256, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.title


class EntityQueue(BaseModel):
    title = models.CharField(max_length=256)
    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class EntityQueueItem(BaseModel):
    weight = models.IntegerField(default=1)
    queue = models.ForeignKey('EntityQueue', on_delete=models.CASCADE)
    service = models.ForeignKey('Services', on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.service.title

    class Meta:
        ordering = ('-weight', 'service__title',)
        unique_together = ('service', 'queue')
