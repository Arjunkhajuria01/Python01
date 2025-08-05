# Docstrings are not comments they are written just above the particular function and they can we called in output 
def square(n):
  '''Takes in a number n, returns the square of n'''
  print(n**2)
square(5)
print(square.__doc__)

