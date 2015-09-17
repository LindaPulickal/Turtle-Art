import turtle

def drawStrand(myTurtle, branchLen):
	"This function draws 1 strand of the snowflake"
	myTurtle.forward(branchLen)
	smallBranchLen = branchLen * 0.40
	myTurtle.backward(smallBranchLen)
	myTurtle.right(30)
	goAndComeBack(myTurtle, smallBranchLen)
	myTurtle.left(60)
	goAndComeBack(myTurtle, smallBranchLen)
	myTurtle.right(30)
	myTurtle.backward(branchLen - smallBranchLen)

def goAndComeBack(myTurtle, distance):
	"This function moves the turtle forward by distance and brings it back"
	myTurtle.forward(distance)
	myTurtle.backward(distance)

def main():
	myTurtle = turtle.Turtle()
	screen = turtle.Screen()
	turtle.bgcolor("lightblue")
	myTurtle.color("white")
	myTurtle.width(10)
	
	for i in range(0,360,30):
		drawStrand(myTurtle,100)
		myTurtle.left(30)
		
	myTurtle.hideturtle()
	screen.exitonclick()	

if __name__ == '__main__':
	main()
