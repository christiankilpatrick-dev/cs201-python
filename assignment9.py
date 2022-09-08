#CS 201 Assignment 9 -- Fun with Funding

import csv
import datetime



def totals_by_year(directorate):
    #open Awards.csv file
    with open('Awards.csv', 'r') as Awards_csv:
        Awards_reader = csv.reader(Awards_csv)
        Awards = list(Awards_reader)
        
        #Use header row to determine indices of: StartDate, AwardedAmountToDate, NSFDirectorate
        header = Awards[0]
        year_col = header.index('StartDate')
        funds_col = header.index('AwardedAmountToDate')
        directorate_col = header.index('NSFDirectorate')
        
        awards_dict = {}
        
    for row in range(1, len(Awards)):
        #read the 3 columns 
        year = int(datetime.datetime.strptime(Awards[row][year_col], '%m/%d/%Y').year)
        #compute the year of StartDate. If earlier than 1990, ignore.
        #if NSFDirectorate not a directorate, ignore row.
        #keep a running total, by year, of all grants' AwardedAmountToDate that year for that directorate
        #return a dictionary with: keys = years, values = total annual grants for that directorate
        if year > 1989 and Awards[row][directorate_col] == directorate:
            funds = float(Awards[row][funds_col].strip('$').replace(',', ''))
            if year in awards_dict.keys():
                awards_dict[year] = awards_dict[year] + funds
            else:
                awards_dict[year] = funds
    return awards_dict



