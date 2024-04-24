from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('create/', UserListCreateAPIView.as_view(), name='create'),
]
