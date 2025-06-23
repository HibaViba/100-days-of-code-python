from turtle import Turtle,Screen
import random

object1=Turtle()
object2=Screen()
############# TRIANGLE, Square , khumassi , sudassi , suba3i
#i=3
#while i <=10:
#
#    for key in range (i):
#        object1.right(360/i)
#        object1.forward(100)
#    i=i+1
#    object2.colormode(255)
#    object1.color((random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))

################## RANDOM WALK #########################

#r=random.randint(0, 255)
#g=random.randint(0, 255)
#b=random.randint(0, 255)
#object2.colormode(255)
#object1.pensize(10)


#def random_left_right(a):
#    if a == 0:
#        return object1.right(90)
#    elif a == 1:
#        return object1.left(90)
#object1.speed("fastest")
#for i in range (100):
#    object1.color((random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))
#    object1.forward(20)
#    #object1.right(90)
#    random_left_right(random.randint(0,1))
#    object1.forward(20)

#####################"Make a spirograph################"
#object2.colormode(255)
#object1.speed("fastest")
#for i in range (80):
#    object1.right(360) #instead of usin right left so the turtle turn around itself , u can use this function object1.heading()+size_of_gap
#    object1.circle(100)
#    object1.left(355)
#    object1.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

import colorgram
colors = colorgram.extract('spots.jpeg', 30)
object2.colormode(255)
list=[]
print (colors)
for key in colors:
    rgb = key.rgb
    list.append((rgb.r,rgb.g,rgb.b))
#print (list)

object1.speed("fastest")
object1.penup()
object1.hideturtle()
step=50
for j in range (11):
    #object1.penup()
    object1.goto((-1000//2), (540//2)-step)
    #object1.pendown()

    for i in range(20):
        object1.fillcolor(random.choice(list))

        #object1.penup()
        object1.forward(50)
        #object1.pendown()

        object1.begin_fill()
        object1.circle(10)
        object1.end_fill()
    step=step+50





#print(object2.window_width())
#print(object2.window_height())







object2.exitonclick()
