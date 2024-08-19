#!/usr/bin/env python3

import pycountry
import argparse

parser = argparse.ArgumentParser("This is a program is for those who love geography")
parser.add_argument('choice', type=int, help='Select a number to display something. - 1: Displays information of a given country. - 2: Displays a list of all available countries by name.')

args = parser.parse_args()


def country_info():
    print("Welcome globetrotter!")
    country = input(f"Enter a country's name to display info. Or 'exit'/'quit' to quit: ")

    value = pycountry.countries.get(name=country)
 
    print(value)
    print("")

    if country == "exit" or country == "quit":
        return 0
    else:
        country_info()

    """
    for country_i in pycountry.countries:
        if country.lower() in country_i.name.lower():
            print(value)
    print("")
    #country_info()
    """

countries_list = []
def country_list():
    for countries in pycountry.countries:
        countries_list.append(countries.name)
    for country in countries_list:
        print(f"Country name is {country}")

countries_list_flags = {}
def country_list_flags():
    for countries in pycountry.countries:
        countries_list_flags[countries.name] = countries.flag
    for country in countries_list_flags.items():
        print(f"Country is: {country[0]} and flag is: {country[1]}")

if args.choice == 1:
    country_info()
elif args.choice == 2:
    country_list()
elif args.choice == 3:
    country_list_flags()
