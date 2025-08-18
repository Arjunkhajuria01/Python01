# marks = [10,20,30,40,70,80]
# def cube(a) : 
#  return a*a*a
#  cube()
# result = list(map(cube , marks))
# print(result)

# using lambda with map 

# MAP : map() → Transforms each element of an iterable (changes it somehow).

marks = [10,20,30,40,70,80]
result = list(map(lambda x : x*x*x , marks))
print(result)

# Mappint multiple iterables

# doing sum of values from different lists 
a = [1,3,5,7]
b = [2,4,6,8]
add = list(map(lambda x , y : x+y , a , b))
print(add)

# with built in functions 

elem = ["arjun" , "rajiv" , "bhavan" , "vansh" , "arush" ]
up = list(map(str.upper , elem))
print(up)

# data cleaning 
fruits = ["   apple   ", " banana    ", "  cherry"]
clean = list(map(str.strip , fruits ))
print(clean)

# Mapping with dictionary 






#FILTER : filter() → Selects elements from an iterable (keeps some, discards others).

# the function given to the filter should  always return false or true 





# REDUCE FUNSTION :- reduce() applies a function cumulatively to the items of an 
# iterable (like a list).

# Syntax of REDUCE : - 
from functools import reduce

numbers = [2,3,5,1,8,9,6,7]
result = reduce (lambda x , y : x+y , numbers)
print(result)

result2 = reduce (lambda x,y : x*y , numbers)
print(result2)


# with initializer 

num = [1,2,3]
result3 = reduce (lambda x , y : x+y, num , 10)    # Starts from 10   works as -> (((10+1)+2)+3) = 16
print(result3)
