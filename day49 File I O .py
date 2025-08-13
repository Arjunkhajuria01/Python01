# FILE HANDELING 
# Opening a file 
#f = open('day31 Sets.py','r' )
#text = f.read()
#print(text)
#f.close()

# if you open a file that does not exist, in write mode , the new file will be created 
f = open('day31 Sets.py','a' )
f.write("This will be added at the last of the file ")
f = open('day31 Sets.py','r' )
text = f.read()
print(text)
f.close()

with open( 'day31 Sets.py', 'w') as f:
 f.write ("Hey im inside the file")
 


