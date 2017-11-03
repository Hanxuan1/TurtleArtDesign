import turtle
from mydesign import*
from random import*

sc=turtle.Screen()
sc.bgcolor('black') #Screen color to black

bob=turtle.Turtle() 

bob.speed(0) #Speed that design be draw

turtle.colormode(255) #To put color through 0 - 255 in to design



main_design(bob) #Main design that start at (0,0)

jump(bob,108,50)
part_main_design(bob) #jump color circle to surround main design

jump(bob,-400,230)
first_design(bob) #Jump first design to top left

jump(bob,400,230)
second_design(bob) #Jump second design to top right

jump(bob,-400,-230)
third_design(bob) #jump third design to bottom left

jump(bob,400,-230)
fourth_design(bob) #jump third design to bottom right

jump(bob,1500,1500) #jump point out of screen to help design look clear
