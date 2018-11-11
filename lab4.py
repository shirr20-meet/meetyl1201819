class animel(object):
	def __init__(self,sound,name,age,food):
			self.sound= sound
			self.name= name
			self.age= age
			self.food= food
	def eat(self):
			print("yummy!! " + self.name + "is eating " + self.food)
	def description(self):
			print(self.name + " is " + self.age + " years old and loves to eat  " + self.food)	

j = animel("roar "," Lionel ", " 5 ", " strawberries")
j.description()



