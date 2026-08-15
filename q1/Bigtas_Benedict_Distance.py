import math

x_1 = float(input("Enter value for x1: "))
y_1 = float(input("Enter value for y1: "))
x_2 = float(input("Enter value for x2: "))
y_2 = float(input("Enter value for y2: "))

minusx = x_2 - x_1
minusy = y_2 - y_1
pow1 = pow(minusx, 2)
pow2 = pow(minusy, 2)
plusagain = pow1 + pow2
distance = math.sqrt(plusagain)
rounded_distance = round(distance, 2)

print("The distance between the two points is: ", rounded_distance)

# Using a programming library is more practical than writing calculations from scratch because it saves time, prevents errors, and uses code that experts have already tested and made fast. In this case, without the math library, I would have to do very complicated pieces of code in order to accomplish this instead of using simple commands to do it for you.
