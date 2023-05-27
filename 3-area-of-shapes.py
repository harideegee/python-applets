# Area of a 2D shape calculator
import math

print("Supported shapes: rectangle, triangle, circle, square, trapezoid, parallelogram")

shape = input("Enter the shape to test: ").lower()

try:
    match shape:
        case "rectangle":
            l = int(input("Enter length: "))
            w = int(input("Enter width: "))
            area = l*w
        case "triangle":
            b = int(input("Enter base: "))
            h = int(input("Enter height: "))
            area = 0.5*b*h
        case "circle":
            r = int(input("Enter radius: "))
            area = math.pi * r * r
        case "square":
            s = int(input("Enter side: "))
            area = s * s
        case "trapezoid":
            a = int(input("Enter length of parallel side 1: "))
            b = int(input("Enter length of parallel side 2: "))
            h = int(input("Enter height: "))
            area = 0.5*(a+b)*h
        case "parallelogram":
            b = int(input("Enter base: "))
            h = int(input("Enter height: "))
            area = b*h

    print(f"Area: {round(area, 2)}")

except:
    print("There was an error. Please retry.")