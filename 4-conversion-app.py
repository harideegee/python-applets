# Basic Feet-Inches to Metres convertor

feet_inches = input("Enter a value in the format '<feet><space><inches>': ")

def convert(feet_inches):
    measurements = feet_inches.split(" ")
    try:
        feet = float(measurements[0])
        inches = float(measurements[1])

        metres = (feet * 0.3048) + (inches * 0.0254)

        return metres
    except:
        return 0
    

value = round(convert(feet_inches), 2)
if value != 0:
    print(f"Result: {value}m")
else:
    print("Please enter appropriate values.")