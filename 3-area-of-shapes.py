# Area of a 2D shape calculator
import math

print("Supported shapes: rectangle, triangle, circle, square, trapezoid, parallelogram")

shape = input("Enter the shape to test: ").lower()

try:
    match shape:
        case "rectangle":
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))
            area = l*w
        case "triangle":
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            area = 0.5*b*h
        case "circle":
            r = float(input("Enter radius: "))
            area = math.pi * r * r
        case "square":
            s = float(input("Enter side: "))
            area = s * s
        case "trapezoid":
            a = float(input("Enter length of parallel side 1: "))
            b = float(input("Enter length of parallel side 2: "))
            h = float(input("Enter height: "))
            area = 0.5*(a+b)*h
        case "parallelogram":
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            area = b*h

    print(f"Area: {round(area, 2)}")

except:
    print("There was an error. Please retry.")