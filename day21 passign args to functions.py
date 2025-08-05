#ARGUMENTS 
# There are 4 types of arguments that we can provide in a function 

# Default argument
# keyword argument 
# variable length argument 
# keyword argument 

# 1) Default Arguments 

# def currency(india = "rupee", america = "dollar", china = "yen"):
#     print("The currency of India is :",india )
#     print("The currency of America is :", america)
#     print("The currency of China is :", china)

# currency("chappal", "joota", "moza")

# SO above is the example of Default arguments , there rupee , dollar , and yen 
#were default arguments , which change acutomatically if some new arguments are 
#provided later while calling them 


# 2) Keyword Arguments 
# basically when you use " = "while giving arguments as above then you dont have to care about order 
# here is the example 
# def currency(india = "Vinod", america = "kumar", china = "khajuria"):
#     print("The name is ", india ,america ,china)

# currency()

# currency(america = "rampal", china = "khajuria", india = "Arjun")
  

# 3) Required arguments 
# When an argument dosent have a required value and it has to be give some value when its called .

# def arjunrampal(a , b = 20):
#     print(a*b)

# arjunrampal(a=4) #it would throw error if value of a is not provided






# including the fucntions for personal preferences 
