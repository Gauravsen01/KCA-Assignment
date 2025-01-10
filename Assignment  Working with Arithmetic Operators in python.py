#!/usr/bin/env python
# coding: utf-8

# ## 1. Basic Calculator  

# In[4]:


a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))

#addition
print("Addition:", a+b)

#subtraction
print("subtraction:", a-b)

#multiplication
print("multiplication:", a*b)

#division
print("division:", a/b)

#modulus
print("modulus:", a%b)

#exponentiation
print("exponentiation:", a**b)

#floor division
print("floor division:", a//b)


# ## 2. Circle Area and Circumderence

# In[7]:


# Note: the value of the pi is 3.14159265359
# In both the cases we used the basic formulas, for area of circle (pir^2) and for circumference of circle (2pir)

radius = int(input("Enter the radius of the circle:"))

print("1. Circumference of the cirle :", 2*3.14159265359*radius)
print("2. Area of the circle :", 3.14159265359*radius**2 )


# ## 3. Rectangle Perimeter and Area

# In[ ]:


# In order to print the area of rectangle we need do basic math, by just multiplying length and width we can calcualte the area of the rectangle.
# In order to print the perimeter of rectangle, we add the length and the width and square it to get the result.

length = int(input("Enter the length of the rectangle"))
width = int(input("Enter the width of the rectangle"))

print("1. Area of the rectangle :", length*width)
print("2. Perimeter of the rectangle :", (length+width)*2 ) 


# ## 4. Average of Numbers

# In[8]:


#Taken input from the user 3 times and to print average of all three number using arithmetic operators we used addition and division.

a = int(input("Enter 1st number :"))
b = int(input("Enter 2nd number :"))
c = int(input("Enter 3rd number :"))

print("Average of the Given three numbers  :is", a+b+c/3)


# ## 5. Unit Conversion (Celcius to Fahrenheit)

# In[5]:


# taking input from the user in celcius

celcius = int(input("Enter the temperature in Celsius : "))

print("Temperature in Fehrenheit :", ((celcius*9/5)+32))


# In[ ]:




