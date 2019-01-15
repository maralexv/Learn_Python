
########################## LINKED LIST  #######################




##########################   STACK   ##########################




##########################   QUEUE   ##########################




##########################   GRAPH   ##########################

class Stack():

	# Initialise stack array
	def __init__(self):
		self.items = []

	# Check if empty - returms True if empty
	def is_empty(self):
		return self.items == []


	# Add item on top
	def push(self, item):
		self.items.insert(0, item)


	# Remove top item
	def pop(self):
		return self.items.pop(0)

	# Make Stack printable for visual output 
	def __repr__(self):
		return f"{self.items}"


##########################   MATRIX   ##########################

