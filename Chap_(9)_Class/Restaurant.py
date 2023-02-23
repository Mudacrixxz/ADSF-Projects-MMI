class Restaurant1:
	"""A simple attempt to model a restaurant."""
	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize restaurant_name and cuisine_type attributes."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
	def describe_restaurant(self):
		"""Describing the restaurant"""
		print(f'-{self.restaurant_name} restaurant has great decor and ambiance...')
		print(f'-Welcome to {self.restaurant_name} retuarant, you will find happiness and best {self.cuisine_type} meal, {self.number_served} customers has been served so far\n')
	def open_restaurant(self):
		"""Informing people that it's now open"""
		print(f"Get ready {self.restaurant_name} is now open for business!\n")

	def set_number_served(self, num):
		'''Set the number of customers that have been served'''
		if num > self.number_served:
			self.number_served = num
		else:
			print('We only move forward!!')

	def increment_number_served(self, add):
		'''Increase the number of customers served by an amount'''
		if add > 0:
			self.number_served += add
		else:
			print('We can\'t reduced customers serving ')
