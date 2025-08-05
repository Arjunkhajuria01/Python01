#The if `__name__ == "__main__"` idiom is a common pattern used in Python scripts to determine whether the script is being run directly
#  or being imported as a module into another script.


# eg /syntax 

def main():
    # Code to be run when the script is run directly
    print("Running script directly")

if __name__ == "__main__": 
    main()


    # suppose the name of the above functionfile was  def welcome() form the file name Harry.py 
    # then the way to import in in now file :-

# import harry

# harry.welcome()
