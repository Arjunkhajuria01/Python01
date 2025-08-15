# marks = [10,20,30,40,70,80]
# def cube(a) : 
#  return a*a*a
#  cube()
# result = list(map(cube , marks))
# print(result)

# using lambda with map 

marks = [10,20,30,40,70,80]
result = list(map(lambda x : x*x*x , marks))
print(result)

