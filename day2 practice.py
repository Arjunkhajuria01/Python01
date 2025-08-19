#STRINGS 

# Q1 ) 
# Take a user’s name as input and print:
# Its length
# The first and last character
# The name in uppercase

# a = input("Enter your name : ")
# print(len(a))

# print(a[0])
# print(a[-1])
# print(a.upper())

#Q2) Given a string:
# s = "python is fun"
# Convert it to title case ("Python Is Fun")
# Count how many times "n" appears

# s = "python is fun"
# print(s.title())
# print(s.count("n"))

#Q3) Reverse the string "hello" without using slicing ([::-1]).
# a = "hello"
# print(a[::-1])
# print(reversed(a))
# rev_a = ""
# for i in a :
#     rev_a = i+rev_a
# 
#print(rev_a)

# Q4) Check if a string is a palindrome (same forward and backward).
# Example: "madam" → True, "python" → False.


# a = "amandnama"
 
# palindrome = True
# for i in range(len(a)):
#  if (a[i] != a[-(i+1)]) :
#   palindrome = False
#   break
 
# if palindrome == True:
#  print("palindrome")
# if palindrome == False:
#  print("not a palindrome")


# Take an email as input and extract the username and domain.
# Example: "arjun123@gmail.com" → username = "arjun123", domain = "gmail.com".

a = input("Enter the email : ")
for i in range(len(a)):
    print(a[i])
    if (a[i+1] == "@"):
        break
    



    














