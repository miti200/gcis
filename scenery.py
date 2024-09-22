""" This program is designed to give the user a choice of picking a flavor for a cake;Pineapple, vanilla, strawberry
    The flavor that is chosen would then be displayed with the cake being on a table and a candle being on top of 
    the cake with a piece of cherry """

# This is the link to Abdulrehman Khalid's github repository : https://github.com/ak2986/SureShot
# This is the link to muhammad eshaans's github repository : https://github.com/me3574/NoTrofy2.0
# This is the link to mitra ranjbar's github repository : https://github.com/miti200/gcis


import turtle as t
def legs(x,length,breadth): #This is eshaans part for this assignment: table
    t.penup()
    t.goto(x,0)
    t.pendown()
    t.fillcolor("brown")
    t.begin_fill()
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(breadth)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(breadth)
    t.end_fill()


def tabletop(length,thickness):
    t.penup()
    t.goto(-(length/2),0)
    t.pendown()
    t.fillcolor("brown")
    t.begin_fill()
    t.forward(length)
    t.left(90)
    t.forward(thickness)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(thickness)
    t.end_fill()
    t.left(90)

def drawtable(tablelength,tablethickness):
    tabletop(tablelength,tablethickness)
    legs(tablelength/2-(tablelength/2*0.1),tablelength/2,tablethickness/2)
    legs(-(tablelength/2-(tablelength/2*0.1)),tablelength/2,tablethickness/2)
    legs(tablelength/3,tablelength/3,tablethickness/3)
    legs(-tablelength/3,tablelength/3,tablethickness/3)

def drawCakeLayer(x,y,fill_color): #This is abdulrehmans part: the cake
    t.speed(1)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(fill_color)
    t.begin_fill()
    t.forward(150)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(50)
    t.end_fill()

def drawCakeCream(x,y,fill_color):
    t.speed(1)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(fill_color)
    t.begin_fill()
    t.left(180)
    t.forward(20)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(20)

def drawCakeLayer2(x,y,fill_color):     
     t.speed(1)
     t.penup()
     t.goto(x,y)
     t.pendown()
     t.fillcolor(fill_color)
     t.begin_fill()
     t.forward(30)
     t.left(90)
     t.forward(100)
     t.left(90)
     t.forward(30)
     t.left(90)
     t.forward(100)
     t.end_fill()

def drawCakeCream2(x,y,fill_color):
     t.speed(1)
     t.penup()
     t.goto(x,y)
     t.pendown()
     t.fillcolor(fill_color)
     t.begin_fill()
     t.left(90)
     t.forward(20)
     t.left(90)
     t.forward(100)
     t.left(90)
     t.forward(20)
     t.left(90)
     t.forward(100)
     t.end_fill()

def circleDecoration(x,y,radius,fill_color):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(fill_color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def Pineapple():
    drawCakeLayer(-80,15,"Yellow")
    drawCakeCream(-80,65,"white")
    drawCakeLayer2(-55,115,"Yellow")
    drawCakeCream2(-55,135,"white")
    circleDecoration(-8,143,4,"red")

def strawBerry():
    drawCakeLayer(-80,15,"red")
    drawCakeCream(-80,65,"white")
    drawCakeLayer2(-55,115,"red")
    drawCakeCream2(-55,135,"white")
    circleDecoration(-8,143,4,"red")

def Vanilla():
    drawCakeLayer(-80,15,"chocolate")
    drawCakeCream(-80,65,"white")
    drawCakeLayer2(-55,115,"chocolate")
    drawCakeCream2(-55,135,"white")
    circleDecoration(-8,143,4,"red")

def draw_candle(x, y, height, width): #This is mitra's part: the candle
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

def Using_Input():
    input("press enter to exit")

def main():
    
    flavor= input("choose a cake flavor (Pineapple, strawberry and vanilla): ")
    drawtable(300,15)
    if flavor== "pineapple":
        return Pineapple()
    elif flavor== "strawberry":    #Used if and elif to be able to give the user a option to choose the cake flavor
        return strawBerry()
    elif flavor== "vanilla":
        return Vanilla()
    

main()
draw_candle(-1, 136, 50, 15) #reason why i called it here and not in main is because it wouldn't work
Using_Input()                #same reason for this
 