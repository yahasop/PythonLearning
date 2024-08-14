#!/usr/bin/env python3

import time #import the library and all its functions

# from time import localtime, mktime, strftime  
# This way we dont need to call the library and only use the specific functions like just in the "function_name()" notation instead of preceding with the library name like in the lib.function() notation

# time functions used in this script
# - localtime()
# - mktime()
# - strftime()

now = time.localtime() # Using methods of the library, in this case to save them to a variable
now_mk = time.mktime(now)


print(now) #Printing the whole output of the method stored in the variable now

print(now_mk)

print(now.tm_hour) # Printing just a value of the method. it is stored in a tuple of dictionaries

print("")


print(f"Timer started at {time.strftime('%X', now)}") #Libraries have methods than can be formatted in a specific way

input("Press Enter to stop timer ")

stop_time = time.localtime() # The input above does nothing more than provide a waiting time difference to set this variable
difference = time.mktime(stop_time) - time.mktime(now)
minutes = (difference / 60)
minutes = round(minutes, 4)

print(f"Timer stopped at {time.strftime('%X', stop_time)}")

print(f"Total time was {minutes} minutes or {int(difference)} seconds.")
