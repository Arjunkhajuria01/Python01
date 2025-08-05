# marks = [2,55,69,87,70,80,20]
 
# index = 0
# for mark in marks :
#     print(mark)
#     if (index == 3):
#      print("MY NAME IS ARJUN")

#     index= index+1
# above is a lengthy method to print somethign between list 

# enumerate is used to solve this problem  ( BASICALLY IT WILL GIVE INDEX ALONG
# with the word in the list , SO WE DONT hAVE TO THINK ABOUT THE INDEX JUST 
# WRITE INDEX, makrs in enumerate(marks ) , thats it , done )
# marks = [2,55,69,87,70,80,20]
 

# for index, mark in enumerate(marks) :
#     print(mark)
#     if (index == 3):
#      print("MY NAME IS ARJUN")


# some more examples 
# names = ["Arjun", "Maya", "Kabir", "Maya", "Rhea"]

# for i, name in enumerate(names):
#     if name == "Maya":
       
#        names[i] = "Mahi"
#        print(names)


words = ["hi", "hello", "hey", "hi", "greetings", "hi"]
# You need to:

# Find all the positions where "hi" appears
# Store those positions (indexes) in a list called hi_indexes

  # [0, 3, 5] eg output 

hi_indexes = []
words = ["hi", "hello", "hey", "hi", "greetings", "hi"]

for index, word in enumerate(words):
    if word == "hi":
     hi_indexes.append(index)
print(hi_indexes)
        



