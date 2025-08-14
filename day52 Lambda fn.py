
# lambda function is used to reduce the syntax of creainf a fucntion for small one liner fucntions 
# basic function creating syntax :- 
# def func (a):
#     x=a*a*a;
#     print(x)

# func(5)

# # using a lambda function for same function:-

# cube = lambda x : x*x*x
# print(cube(5))

# quad = lambda x: x*x*x*x
# print(quad(5))

# lambda fucntions are commonly used as srguments to the higher oreder functions 

nums = [1, 2, 3, 4]
squares = map(lambda x: x ** 2, nums)
print(list(squares))  # [1, 4, 9, 16]
