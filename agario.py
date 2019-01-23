import turtle
import time
import random
import math
from personal_project import Ball

turtle.tracer(0)
turtle.hideturtle()

RUNNING =True
SLEEP= 0.0077
SCREEN_WIDTH =turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

MY_BALL = Ball(0,0,5,9,30,"pink")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 65
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS= []

for B in range (NUMBER_OF_BALLS):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY ,  MAXIMUM_BALL_DY)
	r = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
	color= (random.random(), random.random(), random.random())

	ball = Ball(x,y,dx,dy,r,color)
	BALLS.append(ball)

#making all balls move
def move_all_balls():
	for ball in BALLS :
		ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball_a , ball_b):
	if(ball_a == ball_b):
		return False
	d=math.sqrt(math.pow((ball_b.xcor()-ball_a.xcor()),2) + math.pow(ball_b.ycor()-ball_a.ycor(),2))
	if d <= ball_a.r+ ball_b.r: 
		return True
	else :
		return False

def  check_all_balls_collision():

	for ball_a in BALLS:
		for ball_b in BALLS :
			if collide(ball_a, ball_b):
				r1= ball_a.r
				r2= ball_b.r
				
				x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				if dx ==0 :
					dx= random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)

				dy = random.randint(MINIMUM_BALL_DY ,  MAXIMUM_BALL_DY)
				if dy ==0:
					dy = random.randint(MINIMUM_BALL_DY ,  MAXIMUM_BALL_DY)

				r = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
				color= (random.random(), random.random(), random.random())
				
				if r1>r2:
					r1+=1
					ball_a.r= r1
					ball_a.shapesize(r1/10)
					ball_b.goto(x,y)
					ball_b.dx=dx
					ball_b.dy=dy
					ball_b.r=r
					ball_b.color() 
					ball_b.shapesize(r/10)
				else:
					r2+=1
					ball_b.r= r2
					ball_b.shapesize(r2/10)
					ball_a.goto(x,y)
					ball_a.dx=dx
					ball_a.dy=dy
					ball_a.r=r
					ball_a.color() 
					ball_a.shapesize(r/10)

def check_myball_collision():
	global MY_BALL
	for ball in BALLS :
		if collide(MY_BALL,ball):
			r3= MY_BALL.r
			r4= ball.r
			x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
			y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
			if dx ==0 :
				dx= random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)

			dy = random.randint(MINIMUM_BALL_DY ,  MAXIMUM_BALL_DY)
			if dy ==0:
				dy = random.randint(MINIMUM_BALL_DY ,  MAXIMUM_BALL_DY)

			r = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
			color= (random.random(), random.random(), random.random())
			


			if r3<r4:
				return False
			else:
				r3+=1
				MY_BALL.r = r3
				MY_BALL.shapesize(r3/10)
				ball.goto(x,y)
				ball.dx=dx
				ball.dy=dy
				ball.r=r
				ball.color() 
				ball.shapesize(r/10)
	return True

def movearound(event):
	MY_BALL.goto(event.x - SCREEN_WIDTH, SCREEN_HEIGHT- event.y)

turtle.getcanvas().bind("<Motion>", movearound)
	
turtle.listen()


while RUNNING: 
	SCREEN_WIDTH =turtle.getcanvas().winfo_width()/2
	SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
	turtle.update()
	move_all_balls()
	check_all_balls_collision()
	RUNNING = check_myball_collision()
	time.sleep(SLEEP)







	
