#python program to calculate the area And Circumference of the circle

import math

#taking radius as input from user
radius = int(input("Enter the value of radius of circle in cm :"))

#Calculating Area
area = math.pi*(radius**2)

#calculating Circumference
circumference =2*math.pi*radius

#printing Output

print(f"The area of the given circle is  :{area :.2f} cm²")
print(f"And the circumference of the given circle is  :{circumference :.2f} cm")

