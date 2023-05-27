# Basic Password Strength Checker

print("Conditions for a strong password: \n Must contain at least 8 characters \n Must contain 3 or more numbers \n Must contain at least 1 uppercase letter \n")
password = input("Enter a password: ")
strength = {}


# Length checker

if len(password) >= 8:
    strength["length"]= True
else:
    strength["length"] = False


# Contains Number? checker
digits = 0

for character in password:
    if character.isdigit():
        digits = digits + 1

if digits >= 3:
    strength["digits"]= True
else:
    strength["digits"] = False


# Contains Uppercase? checker
upper = False
for character in password:
    if character.isupper():
        upper = True

strength["uppercase"] = upper

# Password Strength
if all(strength.values()):
    print("Strong Password")
else:
    print("Weak Password")