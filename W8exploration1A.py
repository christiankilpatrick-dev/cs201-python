# Week 8 Exploration 1A

import os
os.chdir("C:\\CS201")

import json

with open('country-by-population.json') as country_file:
    countries = json.load(country_file)


    biggest_country = None
    biggest_country_pop = 0

    for i in countries:
        print('country: ' + i['country'])
        try:
            pop = int(i['population'])
            if (pop > biggest_country_pop or biggest_country is None):
                biggest_country = i['country']
                biggest_country_pop = pop

            print('population: ' + "{:,}".format(pop))

        except:
            print('unkown population')
        print('')


    print('The biggest country is ' + biggest_country + ' at ' + "{:,}".format(biggest_country_pop))

    #OR print(f'the biggest country is {biggest_country} at {biggest_country_pop:,}')
