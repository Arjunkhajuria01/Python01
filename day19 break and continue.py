# break adn continue 

# BREAK :- loop ko shodkr nikal jao 
# CONTINUE :- Iteration ko shodkr nikal jao 

#first creating a table of 5 
i = 0
for i in range(11):
    print("5 X", i , "=", 5*i)
    i = i+1
    
# Now i want it to run only upto 5 then i can use break statement 

    if(i == 5):
     break
print("loop ko shodke nikal jao")



