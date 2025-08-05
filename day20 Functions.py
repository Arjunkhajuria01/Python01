#FUNCTIONS
# Syntax.    :-   def function name ():
def calculategreaternumber(a,b,c):
    if(a>b):
        if(a>c):
            print("First number is greatest")
    elif(b>c):
        if(b>a):
            print("Second number is greatest")
    else:
        print("Third number is greatest")


a=int(input("Enter your first number :"))
b=int(input("Enter your second number :"))
c=int(input("Enter your third number :"))
calculategreaternumber(a,b,c)





