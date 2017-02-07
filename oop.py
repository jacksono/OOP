class Restaurant(object):
	def __init__(self, name="", date_established ="", opening_hours ="", location="")
	self.name = name
	self.date_established = date_established
	self.opening_hours = opening_hours
	self.location = location
	self.service_time = ""

class FastfoodRestaurant(Restaurant):
	"""docstring for FastfoodRestaurant"""
	def __init__(self, opening_hours ="24hrs"):
		self.opening_hours = opening_hours

	def orderChicken(no_of_pieces):
		raise NotImplementedError


class DriveThrough(object):
	"""docstring for DriveThrough"""
	def __init__(self, service_time = "5 minutes"):
		self.service_time = service_time


class FineDining(object):
 	"""docstring for FineDining"""
 	def __init__(self, service_time ="30 minutes"):
 		self.service_time = service_time
 		 
		
		



