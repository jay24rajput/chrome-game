import turtle
import random
from tkinter import *

def drawObstacle(x,y,height):
	turtle.speed(0.5)
	turtle.ht()
	turtle.color('black')
	turtle.setpos(x,y)
	turtle.color('white')
	h=35
	for k in range(3):
		turtle.left(90)
		turtle.forward(h*height)
		turtle.right(90)
		turtle.forward(10)
		turtle.right(90)
		turtle.forward(h*height)
		turtle.left(90)
		if k!=2:
			turtle.forward(10)
		if h==35:
			h=70
		else:
			h=35
	return(x,y,height)

def maketurtle():
	dino=turtle.Turtle()
	dino.setx(-320)
	dino.sety(-120)
	dino.color('white')
	dino.penup()
	return dino

def makewindow():
	window=turtle.Screen()
	window.bgcolor('black')
	return window
def main():
	window=makewindow()
	dino=maketurtle()
	i=0
	x=[]
	height=[]
	lower=-120
	tup=((-290,-200),(-120,20),(100,180),(230,290))
	for k in range(4):
		a,b,c=drawObstacle(random.randint(tup[k][0],tup[k][1]),lower,random.randint(1,4))
		x.append(a)
		height.append(c)
	while True:
		dino.shape('turtle')
		dino.forward(1)
		if dino.xcor()>300:
			dino.ht()
			turtle.clearscreen()
			window=makewindow()
			dino=maketurtle()
			dino.st()
			for k in range(4):
				a,b,c=drawObstacle(random.randint(tup[k][0],tup[k][1]),lower,random.randint(1,4))
				x[k]=a
				height[k]=c
		if dino.xcor()+20 in x:
			dino.setpos(dino.xcor(),(80*height[i])+lower)
			dino.forward(90)
			dino.setpos(dino.xcor(),lower)
			i+=1
			i=i%4
	dino.done()

if __name__ == '__main__':
	main()