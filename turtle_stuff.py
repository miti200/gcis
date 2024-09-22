import turtle

def square():
    turtle.down()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.up()

    def main():
        square(100)
        square(70)
        square(50)
        input("press enter to exit")

    main()

angle= 90

def square(lenght, angle):
    turtle.down()
    turtle.forward(lenght)
    turtle.left(angle)
    turtle.forward(lenght)
    turtle.left(angle)
    turtle.forward(lenght)
    turtle.left(angle)
    turtle.forward(lenght)
    turtle.left(angle)
    turtle.up()

    def main():
        square(100, angle)
        square(75, 120)
        square(50, 150)
        input("press enter to exit")
     

def square():
    turtle.pensize(4)
    turtle.bgcolor ('red')
    turtle.fillcolor("green")
    

