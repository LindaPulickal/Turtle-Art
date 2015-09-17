import turtle

def drawY(myTurle, branchLen):
	"This function draws the Y shape in between 2 petals"
	myTurle.forward(branchLen)
	myTurle.right(30)
	goAndComeBack(myTurle, branchLen)
	myTurle.left(60)
	goAndComeBack(myTurle, branchLen)
	myTurle.right(30)
	myTurle.backward(branchLen)

def goAndComeBack(myTurle, distance):
	"This function moves the turtle forward by distance and brings it back"
	myTurle.forward(distance)
	myTurle.backward(distance)

def main():
	myTurle = turtle.Turtle()
	screen = turtle.Screen()
	angle = 0
	myTurle.color("red")
	for i in range(0,360,30):
		drawY(myTurle,50)
		myTurle.left(30)
	
	myTurle.hideturtle()
	screen.exitonclick()	

if __name__ == '__main__':
	main()
