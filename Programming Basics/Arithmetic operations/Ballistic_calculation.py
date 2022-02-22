from math import sqrt

 
#Define the constant
GRAVITY = 9.8

 
#Read the input from user
h  = int(input())
s = int(input())

 
#Calculate the velocity
velocity = sqrt(2*h/ GRAVITY)*s
x = round(velocity, 2) 

#Display the result
print(f'{x:.2f}')