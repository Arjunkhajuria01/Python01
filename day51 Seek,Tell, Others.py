# Seek() Object 
# seek function is used to move the current position to a specific point the position is stated i bytes 
# and you can move forward or backward from the current porition 
# with open('my files.txt', 'r') as f:
#     text = f.read
#     f.seek(10)
#     position = f.tell() # tell() object 
#     apl =  f.read(5)
#     print(apl)

# Tell() object 
# itis used to tell the current position within the file for eg the location till were you have seeked above it was 10 

    
    #print(position)

# Truncate() Method 
with open('textfile.txt', 'w') as f:
 text = f.write("Hello World")
 f.truncate(5) # limits the size of the text upto th inputed int as 5 is only upto hello , file wil have only hello 

 