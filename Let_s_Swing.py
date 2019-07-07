import turtle

wn = turtle.Screen()


def main():
    wn.setworldcoordinates(-5, -5, 200, 100)
    wn.bgcolor("#66e0ff")

    thuy = turtle.Turtle()
    thuy.color("red")
    thuy.pensize(3)

    def pythagore_triangle(c,b):
        return ((c**2-b**2)**(0.5))

    def draw_rectangle(t,x,y):
       for i in range(2):
            t.right(90)
            t.forward(x)
            t.right(90)
            t.forward(y)

    a= int((pythagore_triangle(80,40)))
    def batdau():
        thuy.left(60)
        thuy.forward(80)

        thuy.right(60)
        thuy.forward(100)

        thuy.right(60)
        thuy.forward(80)

        thuy.penup()
        thuy.right(120)
        thuy.forward(180)

        thuy.right(180)
        thuy.forward(40)
        thuy.left(90)
        thuy.forward(a/4)

        thuy.pendown()
        thuy.forward(a-a/4)

        thuy.penup()
        thuy.right(90)
        thuy.forward(100)

        thuy.pendown()
        thuy.right(90)
        thuy.forward(a-a/4)
        thuy.color("#800000")
        thuy.begin_fill()
        draw_rectangle(thuy,100,10)
        thuy.end_fill()

    batdau()

main()
wn.exitonclick()
