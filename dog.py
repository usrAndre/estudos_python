class Dog:
	species = "Canis familiaris"
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	# Método da instância
	def description(self):
		return f"{self.name} is {self.age} years old"
		
	# Outro método da instância
	def speak(self, sound):
		return f"{self.name} says {sound}"
