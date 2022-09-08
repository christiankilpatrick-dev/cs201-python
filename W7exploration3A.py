import urllib.request
import json

def load_makerspace_list():
  """
  Loads the list of registered MakerSpaces and incubators for Oregon.
  """
  URL = "https://data.oregon.gov/api/views/wpin-z8u6/rows.json?accessType=DOWNLOAD"
  json_string = urllib.request.urlopen(URL).read()
  makerspace_dict = json.loads(json_string)
  return makerspace_dict["data"]

makerspaces = load_makerspace_list()
for makerspace in makerspaces:
  for info_item in makerspace:
    info_item = str(info_item) # in case it's not already a string
    if info_item.find("@") != -1:
      print(info_item)
