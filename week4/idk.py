
import turtle

t=turtle

def candle():
    t.color('red')
    t.fillcolor('red')
    t.begin_fill()
    t.goto(0,max)
    t.goto(min,max)
    t.goto(min,-100)
    t.goto(0,-100)
    t.end_fill()
    t.color('black')
    t.goto(0,100)
    t.goto(0,120)
    t.penup()
    t.goto(2,120)
    t.color('yellow')
    t.pendown()
    t.begin_fill()
    t.circle(8)
    t.end_fill()

def tweak():
    t.speed(0)
    t.tracer(True)
    t.hideturtle()

    def main():
        candle()
        tweak()
    main()

