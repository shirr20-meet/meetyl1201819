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
		new_x = current_x + self.dxcor()
		current_y= self.ycor()
		new_y= current_y + self.dycor()
		right_side_ball = new_x + self.r
		left_side_ball = new_x + self.r
		top_side_ball = new_y + self.r
		bottom_side_ball= new_y + self.r
		self.goto(new_x, new_y)
		if right_side_ball>screen_width:
			self.dx = -self.dx
		if left_side_ball< -screen_width:
			self.dx = -self.dx
		if top_side_ball> screen_height:
			self.dy = -self.dy
		if bottom_side_ball< -screen_height
			self.dy= -self.dy
turtle.mainloop()

		