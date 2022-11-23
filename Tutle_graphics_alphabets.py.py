#!/usr/bin/env python
# coding: utf-8

# In[1]:


#********************************************* ****************************************************************************
#
# Objective: Program will draw 8 different alphabet using Tutle
#           
#***************************************************************************************************************************
import turtle
wn = turtle.Screen()
wn.bgcolor("lightblue")   	# Set the window background color
wn.title("The Alphabets!")     	# Set the window title

onyx = turtle.Turtle()
onyx.color("black")            	# onyx to change the color
onyx.pensize(4)               	# onyx to set the pen width


#s
onyx.penup()
onyx.setpos(-200, 200)
onyx.pendown()

onyx.backward(30)
onyx.right(120)
onyx.forward(15)
onyx.left(45)
onyx.forward(15)
onyx.right(103)
onyx.backward(30)

onyx.left(105)
onyx.forward(15)
onyx.right(45)
onyx.forward(15)
onyx.left(-60)
onyx.forward(30)


#A
onyx.penup()
onyx.setpos(-140, 200)
onyx.pendown()

onyx.left(65)
onyx.forward(60)
onyx.penup()
onyx.setpos(-140, 200)
onyx.pendown()
onyx.right(130)
onyx.backward(60)
onyx.penup()
onyx.setpos(-127, 170)
onyx.pendown()
onyx.right(120)
onyx.backward(21)


#E
onyx.penup()
onyx.setpos(-80, 200)
onyx.pendown()

onyx.forward(40)
onyx.penup()
onyx.setpos(-80, 200)
onyx.pendown()
onyx.right(85)
onyx.forward(55)
onyx.right(-90)
onyx.forward(40)
onyx.penup()
onyx.setpos(-80, 175)
onyx.pendown()
onyx.forward(40)

#C
onyx.penup()
onyx.setpos(10, 200)
onyx.pendown()


onyx.left(180)
onyx.circle(25,180)



#p
onyx.penup()
onyx.setpos(50, 200)
onyx.pendown()
onyx.right(90)
onyx.forward(50)

onyx.penup()
onyx.setpos(50, 200)
onyx.pendown()
onyx.forward(30)
onyx.left(90)
onyx.circle(15,180)
onyx.right(180)


#Y
onyx.penup()
onyx.setpos(130, 200)
onyx.pendown()

onyx.right(110)
onyx.forward(55)
onyx.backward(25)
onyx.right(110)
onyx.forward(35)


#T

onyx.penup()
onyx.setpos(180, 200)
onyx.pendown()

onyx.right(-40)
onyx.forward(40)
onyx.backward(20)
onyx.right(-90)
onyx.forward(50)


#o
onyx.penup()
onyx.setpos(200, 170)
onyx.pendown()
onyx.circle(25,360)






wn.mainloop()






# In[ ]:




