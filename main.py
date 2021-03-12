"""
Header comments
"""
import math

def cube(a):
    return a ** 3 

def area_of_circle(r):
    return math.pi * r**2

if __name__ == "__main__":
    print(cube(3))
    print(f"The area of the circle with radius 3 is {area_of_circle(3):0.2f}")