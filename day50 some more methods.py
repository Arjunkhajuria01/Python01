# read(), readlines() and other methods

# Readlines Method 

f = open('my files.txt', 'r')
# while (True):
#  text = f.readline()
#  print(text)
#  if not text :
#   print(text , type(text))
#   break
 

 # Writelines method 
 # 
f = open('my files.txt', 'w')

lines = ['Line1 \n ',' Line 2 \n ', 'Line 3 \n' ]
f.writelines(lines)
f.close()

