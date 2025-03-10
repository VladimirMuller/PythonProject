from django.urls import path
from .views import get_orders, create_order, get_waypoints, get_waypoints_for_orderId

urlpatterns = [
     path('orders', get_orders, name='get_orders'),
     path('orders/create', create_order, name='create_order'),
     path('waypoints', get_waypoints, name='get_waypoints'),
     path('orders/<int:pk>/waypoints', get_waypoints_for_orderId, name='get_waypoints_for_orderId')
]
