#!/usr/bin/env python
# coding: utf-8

# In[14]:


#*************************************************************************************************************************
#
#Objective: Program will take user input for date and output's corresponding season
#
#**************************************************************************************************************************

print('Enter desired month:', end = ' ')
month = str(input())

print('Enter desired date:', end = ' ')
date = int(input())

spring = ['April','april','May','may']
summer = ['July', 'july', 'August', 'august']
autumn = ['October', 'october','November','november']
winter = ['January','january','February','february', ]

month_1 = ['April','april','june', 'June', 'September', 'september', 'November','november']
month_2 = ['January','january', 'March','march','May','may','July', 'july', 'August', 'august','October', 'october',
'December', 'december']

if ((month in month_1) and (1 <= date <= 30)) or ((month in month_2) and (1<= date <=31)) or (month == 'february' and (1<= date <= 28)):
    
    if (((month == ('march'or'March'))) and (date >= 20)) or ((month == ('june'or'June')) and (date <= 20)):
            print('The output is: \n       Spring')
    if (((month == ('june'or'June'))) and (date >= 21)) or ((month == ('September'or'september')) and (date <= 21)):
            print('The output is: \n       Summer')
    if (((month == ('September'or 'september'))) and (date >= 22)) or ((month == ('December'or 'december')) and (date <= 20)):
            print('The output is: \n       Autumn')
    if (((month == ('December'or 'december'))) and (date >= 21)) or ((month == ('March'or 'march')) and (date <= 19)):
            print('The output is: \n       Winter')
            
    if month in spring:
        print('The output is: \n       Spring')
            
    elif month in summer:
        print('The output is: \n       Summer')
    
    elif month in autumn:
        print('The output is: \n       Autumn')
    
    elif month in winter:
        print('The output is: \n       Winter')

else: print('The output is: \n       Invalid')


# In[ ]:




