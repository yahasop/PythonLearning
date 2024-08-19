#!/usr/bin/env python3

import pycountry
import argparse

parser = argparse.ArgumentParser("This is a program is for those who love geography")
parser.add_argument('choice', type=int, help='Select a number to display something. - 1: Displays information of a given country. - 2: Displays a list of all available countries by name.')

args = parser.parse_args()

def country_info():
    print("Welcome globetrotter!")
    
    while True:
        country_input = input("Enter a country's name to display info. Or 'exit'/'quit' to quit: ").strip()

        if country_input.lower() in ["exit", "quit"]:
            break

        # Initialize a list to store matching countries
        matching_countries = []

        # Search for countries that contain the input string (case-insensitive)
        for country in pycountry.countries:
            if country_input.lower() in country.name.lower():
                matching_countries.append(country)

        if matching_countries:
            # Display all matching countries
            for match in matching_countries:
                print(f"Match found: {match}")
        else:
            print("No matching countries found. Please try again.")

        print("")  # Add an empty line for better readability
        
countries_list = []
def country_list():
    for countries in pycountry.countries:
        countries_list.append(countries.name)
    for country in countries_list:
        print(f"Country's name is '{country}'")

countries_list_flags = {}
def country_list_flags():
    for countries in pycountry.countries:
        countries_list_flags[countries.name] = countries.flag
    for country in countries_list_flags.items():
        print(f"Country's name is '{country[0]}' and flag is: {country[1]}")

if args.choice == 1:
    country_info()
elif args.choice == 2:
    country_list_flags()
elif args.choice == 3:
    country_list()
