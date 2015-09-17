import turtle

def drawPetal(myTurle, branchLen):
	myTurle.forward(branchLen)
	myTurle.right(30)
	goAndComeBack(myTurle, branchLen)
	myTurle.left(60)
	goAndComeBack(myTurle, branchLen)
	myTurle.right(30)
	myTurle.backward(branchLen)

def goAndComeBack(myTurle, distance):
	myTurle.forward(distance)
	myTurle.backward(distance)

def main():
	myTurle = turtle.Turtle()
	screen = turtle.Screen()
	angle = 0
	myTurle.color("red")
	for i in range(0,360,30):
		drawPetal(myTurle,50)
		myTurle.left(30)
	
	myTurle.hideturtle()
	screen.exitonclick()	

if __name__ == '__main__':
	main()
