# try :
#     l = [1,2,3,4,5]
#     i = int(input("Enter the text :"))
#     print(l[i])
# except :
#     print("There is some error")

# finally:
#     print("I am always executed")

#     # you may think that if we directly write print("BLA BLA BLA ") it will also get executed whenever we run code 


# try :
#     l = [1,2,3,4,5]
#     i = int(input("Enter the text :"))
#     print(l[i])
# except :
#     print("There is some error")

# print("I WILL ALSO GET EXECUTED ALWAYS SO WHY USE FINALLY")

# DIFFERENCE KAHAN PR NAZAR AATA :-
def func1():

 try :
    l = [1,2,3,4,5]
    i = int(input("Enter the text :"))
    print(l[i])
    return 0
 except :
    print("There is some error")
    return 1

 print("I WILL ALSO GET EXECUTED ALWAYS SO WHY USE FINALLY")    
    


x= func1
print(x)
    


