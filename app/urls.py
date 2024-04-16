from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .swagger import schema_view
from .views import *

app_name = 'app'

router = DefaultRouter()
router.register(r'passport', PassportViewSet)
router.register(r'passport-data-structure', PassportDataStructureViewSet)
router.register(r'business-glossary', BusinessGlossaryViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('search/', SearchResultsAPIView.as_view(), name='search_results'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
