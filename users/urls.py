from django.urls import path
from .views import UserListCreateAPIView

app_name = 'users'

urlpatterns = [
    path('create/', UserListCreateAPIView.as_view(), name='create'),
]
