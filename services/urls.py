from django.urls import path, include

from rest_framework.routers import DefaultRouter

from services import views

router = DefaultRouter()
router.register(r"services", views.ServiceViewSet)
router.register(r"categories", views.CategoryViewSet)
router.register(r"synonyms", views.SynonymViewSet)

urlpatterns = [
    path('', include(router.urls))
]
