import turtle

# creating object of Screen and Turtle class
s = turtle.Screen()
t = turtle.Turtle()

t.speed(5)

#Here Creating Diagrams
def rectangle (color):
    t.begin_fill()
    t.fillcolor(color)
    for i in range(2):
        t.forward(400)
        t.right(90)
        t.forward(70)
        t.right(90)
    t.end_fill()

s.bgpic("india.gif")
s.bgcolor("yellow")

turtle.title("National Flag Of India ")
t.penup()
t.pensize(15)
t.pencolor("brown")
t.goto(0,-350)
t.pendown()
t.goto(0,350)
t.pensize(2)
t.pencolor("black")
rectangle("orange")
t.goto(0,280)
rectangle("White")
t.forward(200)
t.pencolor("blue")
t.circle(-35)
t.setheading(270)
t.forward(35)
t.setheading(0)
for i in range(24):
    t.forward(35)
    t.backward(35)
    t.left(15)

t.color("black")
t.up()
t.goto(0,210)
t.down()
rectangle("green")
t.up()
t.goto(0, -100)
t.color('red')
t.settiltangle(90)
font_style=("Arial", 25, "bold")
t.write("..Our Lovely India's National Flag..", align="center",font=font_style)

s.exitonclick()