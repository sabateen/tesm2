#!/usr/bin/env python
# coding: utf-8

# # Question 1
# Write a Python program to count the number of characters (character frequency) in a string.
# 
# Examble: ('google.com') =>  {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
# 

# In[21]:


x='googel'
r={'g':x.count('g'),'o':x.count('o'),'e':x.count('e'),'l':x.count('l')}
print(r)


# # Question  2

Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

Examble => 'restart' => 'resta$t'
           'google'  => 'goo$le'
# In[28]:


x='googel'
ch=x[0]
x=x.replace(ch,'$')
x=ch+x[1:]
print(x)


# # Question 3
Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
Examble : 'abc', 'xyz' => xyc abz
# In[60]:


x='abc'
y='xyz'
#x=x.replace(y,y[0])
xx=x[0:2]+y[-1]
yy=y[0:2]+x[-1]
print(' x --> befor : ',x)
print(' x --> After :',xx)
print('________________________________\n')
print(' y --> Befor : ',y)
print(' y --> After : ',yy)


# # Question 4
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
Examble => ab => ab
        => abc => abcing 
        => string => stringly
# In[1]:


def change():
    r=input(str('please enter the string :'))
    if len(r)>=3:
        if r[-3:]=='ing' or r[-3:]=='ING':
            r+='ly'
        else :
            r+='ing'
    elif len(r)<3:
        r=r
    return(r)
    print(r) 


# In[19]:


change()


# In[4]:


change()


# In[18]:


change()


# # Question 5

# Write a Python script to display the various Date Time formats.
# 
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week
# Solution=>
# import time
# import datetime

# In[9]:


import datetime
#current date and time
time=datetime.datetime.now()
print(time)
#current year
print(datetime.datetime.now().year)
#current month
print(datetime.datetime.now().strftime("%B"))
#week number
print(datetime.date.weekday)


# # Question 6

# Write a Python program to print yesterday, today, tomorrow.
# 
# Yesterday :  2020-01-17
# Today :  2020-01-18
# Tomorrow :  2020-01-19
# Solution=>
# import datetime

# In[ ]:





# # Question 7

# 
# Write a Python program to add 5 seconds with the current time.
# 
# 
# Current time=> 13:09:38.491219
# After 5 seconds => 13:09:43.491219

# In[ ]:





# # Question 8

# In[ ]:


Write a Python program to convert Year/Month/Day to Day of Year.


# In[ ]:





# # Question 9
Write a Python program to get current time in milliseconds.
# In[ ]:





# # Question 10
Write a Python program to get week number.
# In[ ]:





# # Question 11
Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
# In[ ]:





# # Question 12

# In[ ]:




Write a Python program to calculate the area of a trapezoid.
# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




