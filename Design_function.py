def polygon(p,dist,sides):    #Function that use to make any polygon
    angle=360/sides
    for times in range(sides):
        p.forward(dist)
        p.left(angle)
    

def part_1(p,size):           #Part of main_design use create main_design 
    times=3
    for times in range(size):
        p.begin_fill()
        polygon(p,times*9,3)
        p.end_fill()
        p.forward(6)
        p.left(6)
        
def main_design(p):            #Main design that create repeat part_1 seven times by color dark to light 
    r=15
    g=2
    b=15
    for times in range(7):
        p.penup()
        p.home()
        p.color(r,g,b)
        p.left(times*60)
        p.forward(times)
        part_1(p,20)
        p.pendown()
        r=r+35
        g=g+5
        b=b+35
        
            
def part_2(p,size):            #Part to create main function
    p.begin_fill()
    polygon(p,50,3)
    p.forward(25)
    p.left(12)
    p.end_fill()


def part_main_design(p):       #Design that surround main design 
    r=5
    g=5
    b=15
    p.penup()
    for times in range(30):
        p.color(r,g,b)
        part_2(p,45)
        p.pendown()
        r=r+2
        g=g+2
        b=b+8
        

def first_design(p):           #Small design that repeat pentagon that star inside on top left of screen
    p.begin_fill()
    for times in range(9):
        p.color(100,250,100)
        polygon(p,75,5)
        p.right(144)
        p.forward(50)
    p.end_fill() 

def second_design(p):          #Small design that repeat pentagon that star inside on top right of screen
    p.begin_fill()
    for times in range(9):
        p.color(250,80,80)
        polygon(p,75,5)
        p.right(144)
        p.forward(50)
    p.end_fill()

def third_design(p):           #Small design that repeat pentagon that star inside on bottom left of screen
    p.begin_fill()
    for times in range(9):
        p.color(200,200,80)
        polygon(p,75,5)
        p.right(144)
        p.forward(50)
    p.end_fill()

def fourth_design(p):          #Small design that repeat pentagon that star inside on bottom right of screen
    p.begin_fill()
    for times in range(9):
        p.color(200,80,200)
        polygon(p,75,5)
        p.right(144)
        p.forward(50)
    p.end_fill()
   
def jump(p,x,y):               #Function that use to jump point to other point
    p.penup()
    p.goto(x,y)
    p.pendown()
