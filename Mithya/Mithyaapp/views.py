from django.shortcuts import render
from .models import Restaurant, FoodItem, Place
from . serializers import RestaurantSerializer, FoodItemSerializer, PlaceSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response


@csrf_exempt
@api_view(("GET",))
@permission_classes((AllowAny,))
def search_obj(request):
	query = request.GET.get("q")
	print(query)
	all_objects = []
	if not query:
		return Response({'message': "search field or string not provided", 'status': 400},status=status.HTTP_400_BAD_REQUEST)
	if query:
		restaurant_objs = Restaurant.objects.filter(restaurant_name__icontains=query).distinct()  
		food_objs = FoodItem.objects.filter(item__icontains=query).distinct() 
		place_objs = Place.objects.filter(place__icontains=query).distinct()
		print(restaurant_objs, food_objs, place_objs)

		for obj in restaurant_objs:
			all_objects.append(RestaurantSerializer(obj).data)

		for obj in food_objs:
			all_objects.append(FoodItemSerializer(obj).data)

		for obj in place_objs:
			all_objects.append(PlaceSerializer(obj).data)
	
		print(all_objects)

	return Response(
	{
	"results": all_objects,
	"status": 200
	},
	status=status.HTTP_200_OK,
	)

