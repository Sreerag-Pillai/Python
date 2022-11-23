#!/usr/bin/env python
# coding: utf-8

# In[17]:


#**********************  Idle_2_temperature.py  *********************
#
# Name: Sreerag M. Pillai
#
# Course: CSCI 1470.01
#
# Assignment: Idle programming assignment #2
#
# Algorythm: Program that mathematiclly analyzes 2 lists of temperature in Webster
#            prompt user to append to the list low_temperature and high_temperature
#            print min,max, mean, of low_temperature and high_temperature
#            pop and remove specific element from low_temperature and high_temperature respectively.
#      ...
#**********************************************************

low_temperature = [29, 30, 32, 39, 39, 40, 44]

high_temperature = [45, 40, 51, 55, 57, 58, 61]

print('Input todays lowest temperature: ', end=' ')
low_temperature.append(int(input()))

print('Input todays highest temperature: ', end=' ')
high_temperature.append(int(input()))

print(f'This week\'s lowest temperature: {min(low_temperature)}')
print(f'This week\'s highest temperature: {max(high_temperature)}')

avg_low= (sum(low_temperature))/(len(low_temperature))
avg_high= (sum(high_temperature))/(len(high_temperature))

print(f'Average of daily low temperatures for the week: {avg_low}')
print(f'Average of daily high temperature for the week: {avg_high}')

diff= avg_high-avg_low

print(f'The difference between average daily low and high temperature for the week: {diff}')

low_temperature.pop(1)
low_temperature.pop(1)
low_temperature.pop(1)

print(low_temperature[1],low_temperature[2])
print(f'Remaining low temperatures: {low_temperature}')
      
high_temperature.remove(40)
high_temperature.remove(55)

print(high_temperature[2])
print(f'Remaining high temperatures: {high_temperature}')


# In[ ]:




