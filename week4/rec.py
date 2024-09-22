import turtle


def rectangle():
    turtle.setPenColor("sandybrown")
    turtle.setFillColor("sandybrown")
    turtle.startPath()
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(72)
    turtle.right(90)
    turtle.forward(72)
    turtle.right(45)
    turtle.forward(100)
    turtle.fillPath()
    turtle.hideTurtle()

    def main():
    rect(50,70)
    rectangle(20,50)
    rectangle(20,50)
    input("press enter to exit")
    main()