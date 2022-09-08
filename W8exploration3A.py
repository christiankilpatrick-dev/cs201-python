#Week 8 Exploration 3A

import os

os.chdir("C:\\CS201")

import csv

def load_birth_death_data():
    #Returns a list of dictionaries,
    #{"state": "Oregon", "county": "Benton", "births": 20, "deaths": 2}

    result = []
    with open('BIRTHDEATH.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_data = list(csv_reader)

        #the first row contains headers
        headers = csv_data[0]
        print(str(len(csv_data)-1)+ ' counties listed')

        index_of_county = headers.index('CHSI_County_Name')
        index_of_state = headers.index('CHSI_State_Name')
        index_of_births = headers.index('Total_Births')
        index_of_deaths = headers.index('Total_Deaths')

        for rownum in range(1, len(csv_data)):
            
            row = csv_data[rownum]

            county = row[index_of_county]
            state = row[index_of_state]
            try:
                births = int(row[index_of_births])
                deaths = int(row[index_of_deaths])

                if (births < 0 or deaths < 0):
                    raise Exception(
                        f'{county}, {state}: {births} births vs {deaths} deaths')

                #print(f'{county}, {state}: {births} births vs {deaths} deaths'}

                result.append({
                    "births": births,
                    "deaths": deaths,
                    "state": state,
                    "county": county
                })
            except: 
                print(
                    f'Discarding {county}, {state} due to missing or invalid data')
    return result

data = load_birth_death_data()

# print the national birth:death ratio

total_births = 0
total_deaths = 0
for county_data in data:
    total_births = total_births + county_data["births"]
    total_deaths = total_deaths + county_data["deaths"]
overall_ratio = total_births/total_deaths
print(f'Overall ratio (births/deaths): {overall_ratio: .2f}')
print()


#calculate each state's ratio
births_by_state = {}
deaths_by_state = {}
for county_data in data:
    state = county_data["state"]
    births_by_state[state] = births_by_state.get(
        state, 0) + county_data["births"]
    deaths_by_state[state] = deaths_by_state.get(
        state, 0) + county_data["deaths"]

for state in births_by_state.keys():
    births = births_by_state[state]
    deaths = deaths_by_state[state]
    ratio = births/deaths

    # show an ASCII bar, length proportional to the ratio
    num_stars = "\u2593"*round(1.75*(ratio))

    print(f' {num_stars}\t {state}: ratio of {ratio:.2f}')


    
                            
