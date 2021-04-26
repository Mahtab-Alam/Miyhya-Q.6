from rest_framework import serializers
from .models import Restaurant, FoodItem, Place

class RestaurantSerializer(serializers.ModelSerializer):

	class Meta:
		model = Restaurant
		fields = '__all__'
		


class FoodItemSerializer(serializers.ModelSerializer):

	class Meta:
		model = FoodItem
		fields = '__all__'
		


class PlaceSerializer(serializers.ModelSerializer):

	class Meta:
		model = Place
		fields = '__all__'
		




