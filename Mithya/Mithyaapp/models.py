from django.db import models

class Restaurant(models.Model):
	restaurant_name = models.CharField(max_length=60)

	def __str__(self):
		return self.restaurant_name

	 


class FoodItem(models.Model):
	item = models.CharField(max_length=50)

	def __str__(self):
		return self.item
	


class Place(models.Model):
	place = models.CharField(max_length=100)
	

	def __str__(self):
		return self.place
