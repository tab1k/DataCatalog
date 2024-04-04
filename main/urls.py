from django.urls import path
from .views import InformationView

urlpatterns = [
    path('', InformationView.as_view(), name='information'),
]

