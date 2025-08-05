# Python Tuples
# Tuples are ordered collection of data items. They store multiple items in a single variable.
#  Tuple items are separated by commas and enclosed within round brackets ().
#  Tuples are unchangeable meaning we can not alter them after creation.

# SYNTAX FOR TUPLE :- 
# (name) = (values)


# example 1 

tupple1 = (1,2,3,4,True , "arjun", 9.10)
print(tupple1)
print(type(tupple1))
print(len(tupple1))
print(tupple1[0 : 7 : 1])


if 1 in tupple1 and 2 in tupple1 : 
    print("Yes 1 and 2 are in tupple 1 ")
else:
    print("They are not present ")

    

    ### Example: Printing all element from a given index till the end
#python
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[4:])      #using positive indexes
print(animals[-4:])     #using negative indexes

### Output:

('pig', 'horse', 'donkey', 'goat', 'cow')
('horse', 'donkey', 'goat', 'cow') 

#When no end index is provided, the interpreter prints all the values till the end.

 

### Example: printing all elements from start to a given index

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[:6])      #using positive indexes
print(animals[:-3])     #using negative indexes

### Output:

('cat', 'dog', 'bat', 'mouse', 'pig', 'horse')
('cat', 'dog', 'bat', 'mouse', 'pig', 'horse')

#When no start index is provided, the interpreter prints all the values from start up to the end index provided. 

 

### Example: Print alternate values

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[::2])     #using positive indexes
print(animals[-8:-1:2]) #using negative indexes

### Output:

('cat', 'bat', 'pig', 'donkey', 'cow')
('dog', 'mouse', 'horse', 'goat')

#Here, we have not provided start and end index, which means all the values will be considered. But as we have provided a jump index of 2 only alternate values will be printed. 

 

### Example: printing every 3rd consecutive withing given range

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[1:8:3])

### Output:

('dog', 'pig', 'goat')

#Here, jump index is 3. Hence it prints every 3rd element within given index.