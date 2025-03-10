from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from django.http import JsonResponse
from rest_framework import status
from .models import Order, Waypoint
from .serializer import OrderSerializer, WaypointSerializer

# from flask import Flask
# from flask_cors import CORS

# app = Flask(__name__)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# Create your views here.
@api_view(['GET'])
#@app.send_wildcard(True)
def get_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
 

@api_view(['POST'])
def create_order(request):
    serializer=OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_waypoints(request):
    waypoints = Waypoint.objects.all()
    serializer = WaypointSerializer(waypoints, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_waypoints_for_orderId(request, pk):
    try:
        order = Order.objects.filter(id = pk).first()
        waypoints = Waypoint.objects.filter(order = order)
        serializer = WaypointSerializer(waypoints, many=True)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response("Either the order doesn't exist.", status=status.HTTP_404_NOT_FOUND)
