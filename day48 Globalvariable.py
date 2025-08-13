# The global variable is one which is initialized outside the function 
# local variable is one which is inside the function 
# when a function is called , if a varibale is both local and global , but have different v
# values then function wil use the global variable 
# to change the value of global variabel , we can use (Global ) keyword inside 
# The function 

x = 10; # here x is a global varibale
print(x)
def gb():
    x = 5 ; # here x is the local varibale 
print(x)
# it would print x = 10 coz it was the global variale 

# calling the function 
gb()


# Using the global keyword 

def gb():
    global x
    x = 19;
    print(x)
# it would print x = 19 coz it was changed using the global keyword 

# calling the function 
gb()