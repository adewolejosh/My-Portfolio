from django.urls import path
from django.views.generic import TemplateView
from .views import SubscribeView

urlpatterns = [
    path('', TemplateView.as_view(template_name='main/home.html'), name='home'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
]
