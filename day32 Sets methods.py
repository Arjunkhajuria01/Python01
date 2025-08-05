s1 = {1,2,5,6}
s2 = {3,6,7}

# Union of two sets 
print(s1.union(s2))
print(s1)
print(s2)
# Updating two sets  , this means s1 ke andar vo values bhi le aao jo s2 me hain aur s1 me nahi hain
#print(s1.update(s2))
print(s1)
print(s2)

# Intersection of two sets 
print(s1.intersection(s2))

# .Intersection_update of two sets 
city1 = {"tokyo","madrid","berlin","delhi"}
city2 = {"tokyo","seoul","kabul","madrid"}
# print(city1.intersection_update(city2))
# print(city1)

# SYMMETRIC DIFFERENCE 
# symmetric_difference--------> creates a new set with the elements from the both the
# sets that are "not common" in between two sets.

# city1 = {"tokyo","madrid","berlin","delhi"}
# city2 = {"tokyo","seoul","kabul","madrid"}
#print(city1.symmetric_difference(city2))  #(common cities are removed, non comman are displayed )

#symmetric difference update  
#just like other updates it will change the set with symmetric difference method
# city1 = {"tokyo","madrid","berlin","delhi"}
# city2 = {"tokyo","seoul","kabul","madrid"}
# print(city1.symmetric_difference_update(city2))
# print(city1)

#DIFFERENCE
#difference------> creates a new set with the elements from a single set that are not common 
print(city1.difference(city2))
#difference_update just like earlier updates


# Some Other Set methods 

# 1) isdisjoint
# sets that have nothing in common 
city1 = {"tokyo","madrid","berlin","delhi"}
city2 = {"tokyo","seoul","kabul","madrid"}
print(city1.isdisjoint(city2))

# 2) issuperset
# set1.issuperset(set2). means every element is set2 is also present in set1 . 
city1 = {"tokyo","madrid","berlin","delhi"}
city2 = {"tokyo","seoul","kabul","madrid"}
print(city1.issuperset(city2))

# 3) issubset
#  checks if a set is subset of another set.
city1 = {"tokyo","madrid","berlin","delhi"}
city2 = {"tokyo","seoul","kabul","madrid"}
print(city1.issubset(city2)) 

# 4) remove
# removes a particular data form set
city1 = {"tokyo","madrid","berlin","delhi"}
print(city1.remove("tokyo"))
print(city1)

# 5) discard 
# works same as remove but wouldnt give error if the data set to be removed is missing from set 
city1 = {"tokyo","madrid","berlin","delhi"}
city1.discard("tokyoo")
print(city1)

# 6) pop
# removes the last element of the set , but since values are stored randomly , random value gets poped
city1 = {"tokyo","madrid","berlin","delhi"}
city1.pop()
print(city1)

# del 
# used to delete  a set 


# in keyword is also used in sets just as in strings and in tupples 
