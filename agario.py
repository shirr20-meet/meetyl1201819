import turtle
import time
import random
from personal.project.py import Ball

turtle.tracer(0)
turtle.hideturtle()

boolean RUNNING set to True
float SLEEP set to 0.0077
SCREEN_WIDTH set to turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT set to turtle.getcanvas().winfo_height()/2

MY_BALL = Ball(0,0,5,9,15,"pink")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = 0
MAXIMUM_BALL_DX = 0
MINIMUM_BALL_DY = 0
MAXIMUM_BALL_DY = 0

BALLS= []

for BALLS in range (5):
	x = random.randit(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randit(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randit(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	dy = random.randit(MINIMUM_BALL_DY ,  MAXIMUM_BALL_DY)
	r = random.randit(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
	color= (random.random(), random.random(), random.random())

ball = Ball(x,y,dx,dy,r,color)
BALLS.append(ball)

#making all balls move
def move_all_balls():
	for ball in BALLS :
		ball.move (SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball_a , ball_b):
	if(ball_a == ball_b):False
		math.sqrt(math.pow((-x1),2) + math.pow((y2-y1),2))




















































































































































































	
