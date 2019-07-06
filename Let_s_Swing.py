import turtle

wn = turtle.Screen()
wn.setworldcoordinates(-5,-5,200,100)
wn.bgcolor("#66ffff")

thuy = turtle.Turtle()
thuy.color("red")
thuy.pensize(3)

def batdau():
    thuy.left(60)
    thuy.forward(100)

    thuy.right(60)
    thuy.forward(100)

    thuy.right(60)
    thuy.forward(100)

    thuy.right(120)
    thuy.forward(160)

batdau()
wn.exitonclick()
