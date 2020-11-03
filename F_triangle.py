import turtle
import math

harm = turtle.Turtle()

def Tangle():
	harm.forward(100)
	harm.left(45)
	# harm.right(45)
	harm.left(45)
	harm.left(45)
	harm.forward(math.sqrt(2)*50)
	for _ in range(2):
		harm.left(45)
	harm.forward(math.sqrt(2)*50)



for _ in range(8):
	Tangle()

