# Tuples are immutable, hence if you want to add, remove or change tuple items, 
# then first you must convert the tuple to a list. Then perform operation on that 
# list and convert it back to tuple.

tuple1 = (0,1,2,3,4,5,6,5,4,3,2,1,0)
# countries = ("America", "spain", "germany" , "India", "switzerland")

# temp = list(countries)
# temp.append("russia")
# print(temp)
# temp.pop(3)
# print(temp)     #india is removed

# temp[2]= "Finland"
# print(temp)
# countries = tuple(temp)
# print(countries)
# print(type(countries))
# print(type(temp))


# but we can directly concatinate 2 or more tuples without converting them to list 

tuple2 = ("arjun", "khajuria", "rampla")
# tuple1.extend(tuple2)            we cannot use extend to concatinate two or more tuples 
# print(tuple1)

tuple3 = tuple1 +tuple2

print(tuple3)