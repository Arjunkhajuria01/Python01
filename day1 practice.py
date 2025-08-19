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

# a = input("enter the Height in centimeters :  ")
# print(type(a))


# b = float(int(a)/100)
# print(b)

# c = int(a)
# print(c)

# Q5) You’re given this list:
# data = ["10", "20.5", "30", "40.75", "hello", "50"]
# Convert all values that can be cast into float and ignore the rest.
# Output should be: [10.0, 20.5, 30.0, 40.75, 50.0].

data = ["10", "20.5", "30", "40.75", "hello", "50"]
# float_values = [float(num) for num in data]
# print(float)      # This is not ignoring hello 

# using for loop 
# for i in data:
#     i = float(i)
#     if (i == "hello"):
#      continue
# print(i)

# gpt method := 
# data = ["10", "20.5", "30", "40.75", "hello", "50"]
# result=[]
# for i in data :
#  try:
#       i = float(i)
 
#  except ValueError:
#   pass
# print(i)

# Q6) Convert a decimal number (e.g., 25) into:
# Binary string ('0b11001')
# Octal string ('0o31')
# Hexadecimal string ('0x19')


# Q7) A user inputs their marks in 5 subjects in one line separated by spaces (string).
# Example: "45 67 89 23 90"
# Convert them into integers and print the average marks.

marks = (input("Enter your marks :"))
marks_list = marks.split()
for mark in marks_list : 
    a = list(int(mark))

print(a)
    















