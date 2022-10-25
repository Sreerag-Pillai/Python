#!/usr/bin/env python
# coding: utf-8

# In[3]:


#**********************  Idle_6_Phone_Numbers.py  ****************************************************************************************************************
#
# Name: Sreerag M. Pillai
#
# Course: CSCI 1470.01
#
# Assignment: Idle programming assignment #5
#
# Algorythm: Program will accept 10 digit phone numeber in xxx-xxx-xxxx format and convert any alphabet in the string into it's numeric equivalent
#
#construction 8 lists with corresponding alphabets
#ABC = ['A', 'B', 'C']
#DEF = ['D', 'E', 'F']
#GHI = ['G', 'H', 'I']
#JKL = ['J', 'K','L']
#MNO = ['M','N','O']
#PQRS = ['P','Q','R','S']
#TUV = ['T','U','V']
#WXYZ = ['W','X','Y','Z']
#
#defining convert function which converts the alphabets in each list listed above into corresponding numeric values
#define convert(x):
#    i = 0
#    for i in x:
#        if i in list ABC:
#            x = x.replace(i, '2')
#        if i in list DEF:
#            x = x.replace(i, '3')
#        if i in list GHI:
#            x = x.replace(i,'4')
#        if i in list JKL:
#            x = x.replace(i, '5')
#        if i in list MNO:
#            x = x.replace(i, '6')
#        if i in list PQRS:
#            x = x.replace(i, '7')
#        if i in list TUV:
#            x = x.replace(i,'8')
#        if i in list WXYZ:
#            x = x.replace(i, '9') 
#    print(f'converted number: {x}')
#
#creating a loop to ask user..
#
#print(f'Enter any key to start or \'stop\' to exit: ',end = ' ')
#exit_input = str(input())
#while exit_input != 'stop':
#code to get user input in the format XXX-XXX-XXXX
#    print("Enter phone number as XXX-XXX-XXXX:", end = '')
#    user_input = str(input())
#    convert(user_input)
#    print(f'Enter any key for another turn or \'stop\' to exit: ',end = ' ')
#    exit_input = str(input())
#    
#*************************************************************************************************************************************************************


#construction 8 lists with corresponding alphabets

ABC = ['A', 'B', 'C']
DEF = ['D', 'E', 'F']
GHI = ['G', 'H', 'I']
JKL = ['J', 'K','L']
MNO = ['M','N','O']
PQRS = ['P','Q','R','S']
TUV = ['T','U','V']
WXYZ = ['W','X','Y','Z']

#defining convert function which converts the alphabets in each list listed above into corresponding numeric values
def convert(x):
    i = 0
    for i in x:
        if i in ABC:
            x = x.replace(i, '2')
        if i in DEF:
            x = x.replace(i, '3')
        if i in GHI:
            x = x.replace(i,'4')
        if i in JKL:
            x = x.replace(i, '5')
        if i in MNO:
            x = x.replace(i, '6')
        if i in PQRS:
            x = x.replace(i, '7')
        if i in TUV:
            x = x.replace(i,'8')
        if i in WXYZ:
            x = x.replace(i, '9') 
    print(f'converted number: {x}')

#creating a loop to ask user..

print(f'Enter any key to start or \'stop\' to exit: ',end = ' ')
exit_input = str(input())
while exit_input != 'stop':
#code to get user input in the format XXX-XXX-XXXX
    print("Enter phone number as XXX-XXX-XXXX:", end = '')
    user_input = str(input())
    convert(user_input)
    print(f'Enter any key for another turn or \'stop\' to exit: ',end = ' ')
    exit_input = str(input())
 


# In[ ]:




