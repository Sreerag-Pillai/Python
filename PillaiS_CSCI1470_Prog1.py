#!/usr/bin/env python
# coding: utf-8

# In[1]:


#**********************  Idle_Weekly_pay.py  *********************
#
# Name: Sreerag M. Pillai
#
# Course: CSCI 1470.01
#
# Assignment: Idle programming assignment #1
#
# Objective: To write a code to find weekly pay of an employee.
#   Prompt user for dayOfWeek
#   Get dayOfWeek
#   if dayOfWeek is Tuesday
#      ...
#**********************************************************
print ('Employee Name: ', end=' ')
employee_name =str(input())

print ('Hourly Wage: ', end=' ')
hourly_wage =float(input())

print ('Total regular hours: ', end=' ')
total_regular_hours = float(input())

regular_pay = (hourly_wage*total_regular_hours)

print ('Overtime hours: ', end=' ')
overtime_hours = float(input())

total_pay= regular_pay + (1.5 * overtime_hours * hourly_wage)

print('Total pay: ', total_pay)

print(employee_name, 'got paid a total pay of:', total_pay)


# In[ ]:




