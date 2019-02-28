from django.contrib import admin
# App Models
from services.models import (
    Categories,
    Services,
    Synonyms,
    EntityQueue,
    EntityQueueItem,
)


# Register your models here.
admin.site.register(Categories)
admin.site.register(Services)
admin.site.register(Synonyms)
admin.site.register(EntityQueue)
admin.site.register(EntityQueueItem)
