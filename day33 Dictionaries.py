#1. Dictionary are using key value pairs to store values
# 2. They are made by using s1={ "key": "value", "key": "value" } syntax
# 3. you can get all keys of dictionary by s1. keys( )
# 4. you can get all values of dictionary by using s1.values( )
# 5. you can get all pairs of dictionary by s1.items( )
# 6. you can get the value of an item by using s1['key'] 
# and it will return the value. s1.get( "key") will also return the 
# value but it wont throw an error in case there is no value/key available in the dictionary

# DICTIONARY
Name = {"name": "Arjun",
         "age" : "13",
           "gender" : "male"}
print(type(Name))

print(Name["name"])

# # or you can use Name,get("key"), also it would not give error if the key is not even in the dictionary 

# # .keys  &   .values
Name = {"name": "Arjun",
         "age" : "13",
           "gender" : "male"}

print(Name.keys())
print(Name.values())

# .items 
Name = {"name": "Arjun",
         "age" : "13",
           "gender" : "male"}

print(Name.items())

for keys,values in Name.items():
    print(f"The value of {keys} in the given dictionary is {values}")
  
 

