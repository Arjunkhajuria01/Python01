# Match Case Statements
# To implement switch-case like characteristics very similar to if-else functionality, we use a match case in python.

# The match case consists of three main entities :

# 1. The match keyword
# 2. One or more case clauses
# 3. Expression for each case

x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")

    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)