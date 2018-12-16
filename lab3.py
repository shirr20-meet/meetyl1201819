import turtle

turtle.register_shape("strawberry.gif")
turtle.shape("strawberry.gif")
roro = 1
turtle.speed(10000)
for i in range(720):
	roro = roro+0.5
	turtle.pendown()
	turtle.right(roro)
	turtle.forward(200)
	turtle.right(45)
	turtle.forward(90)
	turtle.right(80)
	turtle.forward(30)
	turtle.penup()
	turtle.home()
	turtle.goto(0,0)



























turtle.mainloop()