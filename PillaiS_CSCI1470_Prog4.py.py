#!/usr/bin/env python
# coding: utf-8

# In[1]:


#**********************  Idle_4_Turtle.py  ****************************************************************************
#
# Name: Sreerag M. Pillai
#
# Course: CSCI 1470.01
#
# Assignment: Idle programming assignment #4
#
# Algorythm: Program will draw 8 different alphabet
#
#for alphabet s: onyx. penup(), setpos(-200, 200), pendown(), backward(30), right(120), forward(15), left(45), forward(15),
#                right(103), backward(30), left(105), forward(15), right(45), forward(15), left(-60), forward(30)
#
#for alpahbet A: onyx. penup(), setpos(-140, 200), pendown(), left(65), forward(60), penup(), setpos(-140, 200),
#                pendown(), right(130), backward(60)penup(), setpos(-127, 170), pendown(), right(120), backward(21)
#
# for alpahabet E: onyx. penup(), setpos(-80, 200), pendown(), forward(40), penup(), setpos(-80, 200), pendown()
#                  right(85), forward(55), right(-90), forward(40), penup(), setpos(-80, 175), pendown(), forward(40)
#
#for alphabet C: onyx. penup(), setpos(10, 200), pendown(), left(180), circle(25,180)
#
#for alphabet p: onyx. penup(), setpos(50, 200), pendown(), right(90), forward(50), penup(), setpos(50, 200), pendown(), 
#                forward(30), left(90), circle(15,180), right(180)
#
#for alphabet Y: onyx. penup(), setpos(130, 200), pendown(), right(110), forward(55), backward(25), right(110), forward(35)
#
#for alphabet T: onyx. penup(), setpos(180, 200), pendown(), right(-40), forward(40), backward(20), right(-90), forward(50)
#
#for alphabet O: onyx. penup(), setpos(200, 170), pendown(), circle(25,360)
#wn.mainloop()
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




