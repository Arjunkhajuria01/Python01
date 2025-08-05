# a= int(input("ENTER THE VALUE :"))

# if(a>5 or a<9):
#  raise ValueError("There is some value error , value thould be between 5 and 9")

 # Quick quiz. quit input should not give any error for the above code 

a = input("ENTER THE VALUE :")

try:
    a = int(a)
    if 5 < a < 9:
        print(a)
    else:
        raise ValueError("Number not in range")

except ValueError:
    if a == "quit":
        print("You chose to quit.")
    else:
        print("There is some error")

