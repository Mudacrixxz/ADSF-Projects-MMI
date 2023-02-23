class User2:
	"""A simple attempt to model a user."""
	def __init__(self, first_name, last_name, age, address):
		"""Initialize first_name and last_name attributes."""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.address = address
		self.login_attempts = 0
	def describe_user(self):
		"""Describing the user"""
		print(f'His name is {self.first_name} {self.last_name}, he is {self.age} years old.')
		print(f'He lives in {self.address}')
	def greet_user(self):
		"""Greetings"""
		print(f'Good Morning Mr. {self.last_name}, Hope you are doing great?\n')
	def increment_login_attempts(self):
		'''Increase the number of login attempts by 1'''
		self.login_attempts += 1
	def reset_login_attempts(self):
		'''Reset the login_attempts back to zero'''
		self.login_attempts = 0