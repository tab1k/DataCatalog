from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .swagger import schema_view
from .views import DigitalDataViewSet, AttributeDataViewSet, ReferenceInfoViewSet

app_name = 'app'

router = DefaultRouter()
router.register(r'digital-data', DigitalDataViewSet)
router.register(r'attribute-data', AttributeDataViewSet)
router.register(r'reference-info', ReferenceInfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
