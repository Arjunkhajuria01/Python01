# Recursion in python
#Recursion is the process of defining something in terms of itself.

# def factorial(n):
#     if (n==0 or n==1):
#         return 1
#     else :
#         return n * factorial(n-1)    #calling same function inside itself
    


# print(factorial(3))
# print(factorial(6))
# print(factorial(10))

# Creating fibonacci sequence using recursion 
#Fibonacci series :
# f0 = 0 
# f1 = 1 
# f2 = f1 + f0 
# fn = f(n-1) + f(n-2)
# 0 1 1 2 3 5 8 ......
# do we can find fibonacci series like fib series upto 100
def fibonacci(n):
    if (n==0 ):
        return 0
    elif (n==1):
        return 1
    else :
        return (fibonacci(n-1)) + (fibonacci(n-2)) 
    
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
    