from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('orders', views.OrderModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

