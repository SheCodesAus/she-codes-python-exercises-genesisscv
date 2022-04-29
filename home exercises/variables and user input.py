# Q1
number1 = int(input("Enter a number"))
number2 = int(input("Enter another number"))
print(number1 + number2)

number1 = float(input("Enter a number with decimals"))
number2 = int(input("Enter another number"))
print(number1 + number2)

# Q2

number3 = int(input("Enter a number"))
number4 = int(input("Enter another number"))
print(number3 * number4)

number3 = float(input("Enter a number with decimals"))
number4 = int(input("Enter another number"))
print(number3 * number4)

# Q3

distance1 = int(input("How many kilometers"))
meters1 = distance1 * 1000
centimeters1 = distance1 * 100000
print(distance1, "km", "=", meters1, str("m"))
print(distance1, "km", "=", centimeters1, str("cm"))

distance1 = float(input("How many kilometers with decimals"))
meters1 = distance1 * 1000
centimeters1 = distance1 * 100000
print(distance1, "km", "=", meters1, str("m"))
print(distance1, "km", "=", centimeters1, str("cm"))

# Q4

name = str(input("What is your name?"))
height = int(input("How tall are you (cm)?"))
print(name, "is", height, "cms", "tall.")
