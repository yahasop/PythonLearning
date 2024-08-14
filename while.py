#!/usr/bin/env python3


#This is the most basic example of a while loop

count = 0 #A variable to be changed dynamically on every iteration as long as the correct loop is provided
while count <= 4: #This is saying: while var count value is less or equal than four, do the next thing
    print('looping') #The next thing is the two next lines. This one is about printing a message
    count = count + 1 #And this ones is the most important. It says that for every iteration, sum 1 to the value of count.
    #If we dont set a increment, the loop will infintely be looping as the count value will always be less than four.

print("")

#A little bit more complex lop

count =1
while count <= 10: #Our exit condition
    if count % 2 != 0: #A nested if within the while block. This is saying: if the count var value module 2 is 0 (it means is an even number) do the next thing:
        count += 1 #Add 1 to the count value. This is a shorter notation to count = count + 1
    else: #If the previous if doesnt evalueate to true, do this:
        print(f"We're counting even numbers: {count}") #Print something to the screen
        count += 1 #Add 1 to the count value
#The while loop will do whatever is whitin until the condition is met
