from turtle import * 
import turtle

class Ball(Turtle):
	"""docstring for Ball"""
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.r = r
		self.color = color
		
		self.goto(x,y)
		self.shape(circle)
		self.size(r/10)
		self.color(color)

	def move(self, screen_width, screen_height):
		self.screen_height = screen_height
		self.screen_width = screen_width
		current_x= self.xcor()
		new_x = c
		

		