from django.contrib import admin
# App Models
from services.models import Categories
from services.models import Services
from services.models import Synonyms


# Register your models here.
admin.site.register(Categories)
admin.site.register(Services)
admin.site.register(Synonyms)
