import turtle
import time
from turtle import *
import pygame

pygame.mixer.init()
pygame.mixer.music.load("gameover.mp3")
#pygame.mixer.music.play(-1,0.0)


# turtle.Screen().bgpic("clouds(1).gif")
turtle.Screen().bgpic("background(1).gif")
# turtle.Screen().bgpic("galaxy.gif")
turtle.Screen().bgpic('background(1).gif')
score  = 0
SPACEBAR = "space"


def win_game():
	turtle.clear()
	turtle.write("this is Ahmad")
	turtle.Screen().bgpic("ahmad.gif")
	turtle.Screen().bgpic("ahmad.gif")
	# turtle.shape("ahmad.gif")
	#turtle.goto()
	turtle.onkey(win_game2, "space")
def win_game2():
	turtle.clear()
	turtle.write("this is Abed")
	turtle.Screen().bgpic("abed.gif")
	# turtle.shape("abed.gif")
	#turtle.goto()
	turtle.onkey(win_game3, "space")
def win_game3():
	turtle.clear()
	turtle.write("this is Sadek")
	turtle.Screen().bgpic("sadek.gif")
	# turtle.shape("sadek.gif")
	#turtle.goto()
	turtle.onkey(win_game4, "space")
def win_game4():
	turtle.clear()
	turtle.write("this is uriel")
	turtle.Screen().bgpic("uriel.gif")
	# turtle.shape("uriel.gif")
	#turtle.goto()
	turtle.onkey(win_game5, "space")
def win_game5():
	turtle.clear()
	turtle.write("this is gal")
	turtle.Screen().bgpic("gal.gif")
	# turtle.shape("gal.gif")
	#turtle.goto()
	turtle.onkey(win_game6, "space")
def win_game6():
	turtle.clear()
	turtle.write("See you in summer for your first camp!")
	time.sleep(5)
	turtle.quit()

global score
score = score + 1

score =30

if score == 10:
	turtle.Screen().bgpic("clouds(1).gif")
if score == 20:
	turtle.Screen().bgpic("galaxy.gif")
if score == 30:
	RUNNING = False
	turtle.ht()
	turtle.pu()
	turtle.write("Congratulations!, you are now a Y1 MEET student", font=("Arial", 100, "normal"), align="center")
	# turtle.write("click the "space" bar to continue!", font=("Arial",100,"normal"), align="center")
	turtle.listen()
	turtle.onkey(win_game, "space")
	
		# turtle.clear()
		# turtle.ht()
		# turtle.write("MEET your coordinators", font=("Arial", 100, "normal"), align="center")
		# turtle.write("click the "space" bar to continue!", font=("Arial",100,"normal"), align=(0,-100)
		# turtle.onkey(win_game, "space")

			





turtle.mainloop()


