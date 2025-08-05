marks = [3,4,5,"Harry", True , 7,8,9]
print (marks)
# print(type(marks))
# print (marks[0])
# print(marks[1])
# print(marks[4])
# print(marks [-3]) #negative indexing 
# print(marks [len(marks)-3])    #positive indexing 


# print(marks[5-3])    #5-3 = 2

# print(marks[2])

# if (6 ) in marks :
#     print("yes")
# else :
#     print("No")

# # same thing applys for strings also :
# if "harry" in marks :
#     print("yes")
# else :
#     print("No")

# print (marks[0:7])
# print (marks [1 :8])
# print(marks [1:9:3])       # list( start : stop : step)    start at 1  , stop at 9 , and step/ select value at gap of 3


lst = [i*i for i in range(9)]
print(lst)

lst = [i*i for i in range(10) if i%2 == 0] #i%2 ==0 means for i divisible by 2 or just even numbers
print(lst)
