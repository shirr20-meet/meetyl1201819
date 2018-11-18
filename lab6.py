import turtle
from turtle import Turtle
import random
turtle.colormode(255) 


class Square(Turtle):
	def __init__(self, size):
		Turtle.__init__(self)
		self.shape("square")
		self.shapesize(size)

	def random_color(self):
		r= random.randint(0,256)
		b= random.randint(0,256)
		g= random.randint(0,256)

		self.color(r,b,g)




		
x= Square(6)
x.random_color()

turtle.mainloop()

		
	
		