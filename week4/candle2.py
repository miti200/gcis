import turtle
t=turtle

def draw_candle(x, y, height, width):
   t.penup()
   t.goto(x, y)
   t.pendown()
   t.fillcolor("pink") 
   t.begin_fill() 
   t.setheading(90) 
   t.forward(height)  
   t.right(90)
   t.forward(width) 
   t.right(90)
   t.forward(height)  
   t.right(90)
   t.forward(width) 
   t.right(90)
   t.end_fill()
    
   t.penup()
   t.goto(x + width / 2, y + height)
   t.pendown()
   t.setheading(90)  
   t.pensize(2)
   t.forward(15)  
    
   t.penup()
   t.goto(x + width / 2, y + height + 15)
   t.pendown()
   t.begin_fill()
   t.fillcolor("yellow") 
   t.circle(7)  
   t.end_fill()


t.speed(1)
draw_candle(0, 0, 50, 15)
turtle.done()

