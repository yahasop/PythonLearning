#!/usr/bin/env python3


# BMI = (weight in kg / height in meters squared)
# Imperial version: BMI * 703

def gather_info(): #The function does not require arguments
    height = float(input("What is your height? (Inches or Meters) "))
    weight = float(input("What is your weight? (Pounds or Kilograms) "))
    system = input("Are you measurements in metric or imperial units? ").lower().strip()
    #print(system)
    return (height, weight, system) #The return statement is always at the of the function. In this case we save the variables into a tuple to be provided later as arguments to the function

def calculate_bmi(weight, height, system='metric'): #The default system variable will have a default value of 'metric'
    """
    Return the body mass index
    """

    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi

# This conditional will run forever, unless we provide useful information to the script. It basically runs itself every time
while True:
    height, weight, system = gather_info() # This is a tuple unpacking. The gather_info function returns a tuple. This tuple can be multpiple assigned to the three variables in this line.
    if system.startswith('i'):
        bmi = calculate_bmi(weight, system=system, height=height) #This way of passing arguments to the function where we define system=system is when arguments are in no specific order. If we are not setting those that way, they would need to be in order and also expecting N numbers of them
        print(f"Your BMI is {bmi}")
        break
    elif system.startswith('m'):
        bmi= calculate_bmi(weight, height) #Here a system variable is not needed to be provided to the function call as we have stablished a default value for it
        print(f"Your BMI is {bmi}")
        break
    else:
        print(f"Error: Unknown measurement system. Please use imperial or metric.")
