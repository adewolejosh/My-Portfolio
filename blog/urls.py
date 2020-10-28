from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blog-list'),
    path('<slug:slug>/', BlogPostDetailView.as_view(), name='blog-detail'),
    # path('<int:pk>/<slug:slug>/', BlogPostDetailView.as_view(), name='blog-detail'),
    # path('<int:pk>/', BlogPostDetailView.as_view(), name='blog-detail'),
]
