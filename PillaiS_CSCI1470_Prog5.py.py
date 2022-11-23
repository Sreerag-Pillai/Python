#!/usr/bin/env python
# coding: utf-8

# In[11]:


#*********************************************************************************************************************
#
# Objective: Program will give user a math quiz with 10 random questions using 4 mathematical operators
#            and will return their the grades
#           
#***********************************************************************************************************************

import random
# defining arithemic operations
def div(a,b):
    c = a//b
    return c
def mult(d,e):
    f = d * e
    return f
def add(g,h):
    j = g+h
    return j
def sub(k,l):
    m = k - l
    return m
def exp(n,p):
    q = n ** p
    return q

print('Type start or stop: \n')
user_input = str(input())

#A loop which will stop if user enter stop

while user_input != 'stop' or user_input == 'start':
    grade = 0
    ques = 1
    
#construting a for loop nested in the while loop for the quiz
    
    for i in range(10):
        rquest = random.randint(1,5)
        
#Cresting barches for questions related to all five math operations

#Addition
        if rquest  == 1:
            aa = random.randint(1,10)
            ab = random.randint(1,10)
           
            print(f'Q.{ques}: {aa} + {ab} = ')
            ans = int(input())
            if ans == add(aa,ab):
                grade += 1
                print(f'correct total score: {grade}')
            else: print(f'incorrect total score: {grade}')
                      
            ques += 1

#subtraction           
        elif rquest == 2:
            sa = random.randint(1,10)
            sb = random.randint(1,10)
           
            print(f'Q.{ques}: {sa} - {sb} = ')
            ans = int(input())
            if ans == sub(sa,sb):
                grade += 1
                print(f'correct total score: {grade}')
            else: print(f'incorrect total score: {grade}')
            ques += 1

#multiplication
        elif rquest ==3:
            ma = random.randint(1,10)
            mb = random.randint(1,10)
           
            print(f'Q.{ques}: {ma} * {mb} = ')
            ans = int(input())
            
            if ans == mult(ma,mb):
                grade += 1
                print(f'correct total score: {grade}')
            else: print(f'incorrect total score: {grade}')
            ques += 1

#Division
        elif rquest == 4:
            da = random.randint(1,10)
            db = random.randint(1,10)
           
            print(f'Q.{ques}: {da} // {db} = ')
            ans = int(input())
            if ans == div(da,db):
                grade += 1
                print(f'correct total score: {grade}')
            else: print(f'incorrect total score: {grade}')
            ques += 1

#Exponent
        elif rquest  == 5:
            ea = random.randint(1,10)
            eb = random.randint(1,3)
           
            print(f'Q.{ques}: {ea} ^ {eb} = ')
            ans = int(input())
            if ans == exp(ea,eb):
                grade += 1
                print(f'correct total score: {grade}')
            else: print(f'incorrect total score: {grade}')        
            ques += 1
#returning total grade
    total = grade
    print(f'Total: {total}')

#Asking if the user want to take the quiz again
    print(f'Do you want to take another quiz (enter start to start quiz or stop to stop): ')
    user_input = str(input())

#Breaking the loop if the user enters stop    
    if user_input == 'stop':
        break

            
            
            


# In[ ]:




