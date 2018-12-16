#class animel(object):
	#def __init__(self,sound,name,age,food):
			#self.sound= sound
			#self.name= name
			#self.age= age
			#self.food= food
	#def eat(self):
			#print("yummy!! " + self.name + "is eating " + self.food)
	#def description(self):
			#print(self.name + " is " + self.age + " years old and loves to eat  " + self.food)	

#j = animel("roar "," Lionel ", " 5 ", " strawberries")
#j.description()
#j.description()
#j.description()

class person(object):
	"""docstring for person"""
	def __init__(self, name, age, breakfast, activity):
		
		self.name = name
		self.age = age
	
		self.breakfast = breakfast
		self.activity = activity
	
	def eat(self):
		print("hi! " + "my name is " + self.name + "and I'm eating " + self.breakfast)
	def favorite(self):
		print("My name is " + self.name + "and I'm " + self.age +"years old. The thing I like to do the most is " + self.activity)
		

#boo = person("ruru ","10 ","shakshuka ")
#boo.eat()

soo = person("Judy ","48 ","salad", "reading books")
soo.favorite()







