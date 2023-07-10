import math

radius = float(input("Enter the radius of the circle:"))

def calculate_area(radius):
	area = math.pi * radius**2
	print(area)

calculate_area(radius)
