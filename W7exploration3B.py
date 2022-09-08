#Week 7 Exploration 3B (JSONs)


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

output_file = open('makerspaces.csv', 'w', newline='')
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
