#!/usr/bin/env python3
# The shebang above denotes a system-wide use of Python configurations and libraries. We can specify if theres a need to use an specific environment used. This is in order to use the libraries/configurations said environment has and that are not available system-wide

import argparse
import requests #This library and the pycountry needs to be also added to the system/environment with pip install
import pycountry
#import os
#import sys

#Parser block to define our parser, our arguments and a variable to store them.
parser = argparse.ArgumentParser(description='This is a weather application. Provide the city and country as arguments')
parser.add_argument('city', help='City where you want to get weather information, encase it in quotes if its two words')
parser.add_argument('country', help='Country where the city is located, encase it in quotes if its two words')

args = parser.parse_args()

# We make use of the pycountry library to fetch the short name of a country to be provided to the API url
country = pycountry.countries.get(name=args.country) #Countries is a method and get a function of the pycountry library. Then we get the values of the dict instance of that specific country
country_code = country.alpha_2.lower() #This fetches the short value within the alpha_2 value. We then lowercase it

api_key="a71d49ced890684d532899bd159c7622" #default

"""LINES OF CODE IF THE API KEY IS SAVED INTO AN ENVIRONMENT VARIABLE
api_key = os.getenv("WEATHER_API_KEY") #We need to have a WEATHER_API_KEY env variable defined first and with a value equivalent to an actual API key.
#This line above uses the getenv function to fetch, if any, the value of WEATHER_API_KEY

#This line just checks if an API key exists. If not, the program wont work. An exit code of 1 would be returned 
if not api_key:
    print('Missing API key')
    sys.exit(1)
"""

#The API URL. This is how we reach the weather API. It has the city defined as argument and the variable where we converted the other argument to a two digits code. The we fetch the API key from api_key code and lastly we convert to metric system the output.
url = f"https://api.openweathermap.org/data/2.5/weather?q={args.city},{country_code}&APPID={api_key}&units=metric&lang=es"

json_out = requests.get(url).json() #This method of requests has two function attached. The get() curls the API URL and returns an HTTP code, and the json() tranforms the information to a JSON format.

#Then, this is only printing some values of the the JSON output to provide a human readable output to read the weather.
print(f"Current weather in {json_out['name']}, {args.country} is {json_out['main']['temp']} celsius. Expected minimum is {json_out['main']['temp_min']} and maximum is {json_out['main']['temp_max']}")
