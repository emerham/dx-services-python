from django.urls import path, include

from rest_framework.routers import DefaultRouter

from services import views

router = DefaultRouter()
router.register(r"services", views.ServiceViewSet)
router.register(r"synonyms", views.SynonymViewSet)
router.register(r"categories", views.CategoryViewSet)
router.register(r"queueitems", views.EntityQueueItemViewSet)
router.register(r"queues", views.EntityQueueViewSet)

urlpatterns = [
    path('', include(router.urls))
]
