# A program that accepts the user input and generates the area of the circle 

import math

radius = int(input("Enter a radius: "))

def calculate_area(r):
    area =0
    area = math.pi * (r * r)
    return area

print(calculate_area(radius))