# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

print(" CODER / DECODER")


def coder(): 
 text = input("ENTER YOU TEXT :")
# this function will code your input 
# tells characteres separately 
 character = text.split()
 print(character)
# tells the length of each character 
 length1 = [len(word) for word in character]
 print(length1)

# now check which word has length <= 3 or len >3

 for (word) in character : 
  if len(word) <= 3 :
   # now add the method that reverses the string 
   print(''.join(reversed(word)))
  elif (len(word)>3):
    # now add the method that takes first letter of word to last
     modword =  word[1:] + word[0]
     # now we have to add random 3 characters at the end and at the beginning of the modified words
     print(f"ala{modword}xma", end=" ")

coder()

     

 
def decoder():
   # provide separate code for decoder 
  text = input("ENTER YOU TEXT :")
# tells characteres separately 
  character = text.split()
  print(character)

  # tells the length of each character 
  length1 = [len(word) for word in character]
  print(length1)

  #now check which word has length <= 3 or len >3
  for (word) in character : 
   if len(word) <= 3 :
   # now add the method that reverses the string 
    print(''.join(reversed(word)))
   elif (len(word)>3):
    # now add the method that takes first letter of word to last
    modword =  word[0] + word[1:]
     # now we have to add random 3 characters at the end and at the beginning of the modified words
    print(f"ala{modword}xma", end=" ")

decoder()
 




 

 