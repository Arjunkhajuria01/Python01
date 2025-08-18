# TYPE CASTING
# Q1) Take input of your age (string from input()), and:
# Convert it to an integer.
# Add 5 to it and print: “Your age after 5 years will be …”


# a = input("Enter your age")
# print(a)
# print(type(a))

# b = int(a) + 5
# print(f"Your age after 5 years is {b}")


# Q2) Write a program that takes a float number (e.g., 9.81) and converts it into:
# An integer
# A string
# A boolean
 
# a= float(input("Enter the float number"))

# b = int(a)
# c = str(a)
# d = bool(a)
# print(b, c , d)

# Q3) Convert this list of integers into a list of strings using list comprehension:
# numbers = [1, 2, 3, 4, 5]
# Result should look like: ['1', '2', '3', '4', '5'].

# first trying with loops 

# numbers = [1, 2, 3, 4, 5]
# for number in numbers : 
#      a = str(number)
#      b = (list(a))
#      print(b) 
# # using list comprehension 
# new_lsit = [str(num) for num in numbers]
# print(new_lsit)

# Q4) A user enters their height in centimeters as a string. Convert it to:
# Float in meters
# Integer in centimeters
# Example: "175" → 1.75 (meters), 175 (cm as int).

a= input("enter the Height in centimeters :  ")

b = float(int(a)/100)
print(b)






