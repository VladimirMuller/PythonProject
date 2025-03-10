from rest_framework import serializers
from .models import Waypoint, Order

# Serializers for models to JSON.

class WaypointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waypoint
        fields = ("id", "address", "type_address", "order")



class OrderSerializer(serializers.ModelSerializer):
    waypoints = WaypointSerializer(many=True, required=False)

    def create(self, validated_data):
        waypoints_data = validated_data.pop('waypoints')

        order = Order.objects.create(**validated_data)
        for waypoint_data in waypoints_data:
            Waypoint.objects.create(order=order, **waypoint_data)
        return order
    
    class Meta:
        model = Order
        fields = ("id", "number","customer_name","date","waypoints")
        #ordering = ["customer_name"]

