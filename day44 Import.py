#Importing in Python is the process of loading code from a Python module into the current script. 
# This allows you to use the functions and variables defined in the module in your current script, as well as any 
# additional modules that the imported module may depend on.
# first import the module
# import math
# 
# you can import particular functions form a module using for keyword
#eg :- 
# from math import sqrt

# result = math.sqrt(9)
# print(result)  # Output: 3.0

# you can import multiple functions and variable at once by separating them wiht a comma 
# from math import sinh, pi    # like this 


## importing everything
# It's also possible to import all functions and variables from a module using the * wildcard.
# However, this is "generally not recommended as it can lead" to confusion and make it harder 
# to understand where specific functions and variables are coming from.

# eg :- from math import *


# Python also allows you to rename imported modules using the as keyword. 
# import math as m

# The dir function
#Finally, Python has a built-in function called dir that you can use to view the names of all the functions
#and variables defined in a module.
import math
print(dir(math))
