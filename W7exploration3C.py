## Week 7 Exploration 3C

#Like in 3B, this program reads a json from a link and writes desired info to
# a new csv.file. This program then reads back the info on that file at the end.
##THAT LINK is bad, dont try running this program

import urllib.request
import json
import csv

def load_makerspace_list():
  """
  Loads the list of registered MakerSpaces and incubators for Oregon.
  """
  URL = "https://data.oregon.gov/api/views/wpin-z8u6/rows.json?accessType=DOWNLOAD"
  json_string = urllib.request.urlopen(URL).read()
  makerspace_dict = json.loads(json_string)
  return makerspace_dict["data"]

#import file, get info, and write to new csv

FILE_NAME = 'makerspaces.csv'
output_file = open(FILE_NAME, 'w', newline='')
csv_writer = csv.writer(output_file)
csv_writer.writerow(['name', 'phone', 'email'])
makerspaces = load_makerspace_list()
for makerspace in makerspaces:
  if len(makerspace) > 11:
    name = makerspace[8]
    phone = makerspace[10]
    email = makerspace[11]
    csv_writer.writerow([name, phone, email])
output_file.close()

#reading file back

input_file = open(FILE_NAME, 'r')
reader = csv.reader(input_file)
next(reader) #skip first row
for row in reader:
    name = row[0]
    phone = row[1]

    print(name + ' is an Oregonian and has the phone number ' + phone)
    

