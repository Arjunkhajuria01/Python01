# Exception handeling is the process of responding to unwanted or unexpected errors when a program runs 

# print("Enter the number : \n")
# a = (input())


# print(f"The multiplication table of {a} is:\n")

# try:
 
#     for i in range(1 , 11):
#      b = int(a)* i 
#      print ( f"{int(a)} X {i}  = {b}" )
# except Exception as e :
#    print("Some ERROR")


# print("Some lines of code")
# print("End fo code ")

# you can use multiple excepts also 

# some personal practice using chat gpt 

# 1) ZERO DIVISION ERROR  :- Occurs when dividing a number by zero.
 
# print("THE ZERO DIVISION ERROR ")
# try :
#   print(10/0)
# except ZeroDivisionError:
#  print("The value is invalid")

#  print ("THE ZERO DIVISION ERROR AGAIN ")
#  a = int(input("ENTER THE NUMBER :"))
# try :
#    print (a/0)
# except ZeroDivisionError:
#   print ("The value is invalid")

# 2) VALUE ERROR   :- Occurs when a function receives a value of the correct type but inappropriate value.

# try :
#   a = int(input("Enter the value"))
#   print(a)
# except ValueError:
#   print("The Value is Invalid")


# try :
#   a = int(input("ENTER THE AGE :"))
#   if (a<0) :
#     raise ValueError("AGE CANT BE NEGATIVE")
  
# except ValueError as ve:
#   print("ValueError :" , ve)

# else :
#   print(a)

# 3) TYPE ERROR   :- Happens when operations are done between incompatible types.
# try :
#     AGE = int(input("ENTER THE AGE:"))
#     print(AGE + 35)
# except ValueError:
#     print("INVALID INPUT VALUE")



# try:
#     total = sum("12345")
# except TypeError as e:
#     print("TypeError:", e)

# 4) INDEX ERROR  :- Trying to access a list element at a position that doesn’t exist.

# try :
#     data = [1,2,3,4,5]
#     print(data)
#     a = int(input("Enter the value:"))
#     data.pop(a)
#     print(data)
# except IndexError:
#     print("The value is not present")


# 5) KEY ERROR.    :- Trying to access a key that’s not in the dictionary.
#try :
#     person = {"NAME" :"ARJUN"}
#     print(person["age"])
# except KeyError:
#     print ("The key is not present")

# try:
#     marks = {"Math": 90}
#     print(marks["Science"])
# except KeyError as e:
#     print(f"Missing key: {e}")

# 6) FILE NOT FOUND ERROR    :- Trying to open a file that doesn’t exist.

# try:
#     f = open("abc.txt", "r")
# except FileNotFoundError:
#     print("File not found.")

try:
    with open("data.csv") as f:
        content = f.read()
except FileNotFoundError:
    print("Could not open the file.")

# 7) NAME ERROR 



































































