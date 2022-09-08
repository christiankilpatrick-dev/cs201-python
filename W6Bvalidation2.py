#W6BValidation2
#the following code checks if a certain string str is a five-digit zip code


import re
print("Enter a zip code (or not)")
user_input = input()
if re.search('^[0-9]{5}$', user_input):
  print("is valid!")
else:
  print("is not valid")


import re
providers = []
while True:
  provider = {}
  print("Provider name (blank if done entering providers):")
  provider["name"] = input().replace('"', '').strip()
  if len(provider["name"]) == 0:
    break
  print("Provider address (blank if done entering providers):")
  provider["address"] = input().replace('"', '').strip()
  if len(provider["address"]) == 0:
    break
  print("Provider zip code:")
  provider["zip"] = input().strip()
  if not re.search("^[0-9]{5}$", provider["zip"]):
    print("Invalid zip. Discarding and continuing with what we have so far.")
    break
  print("Provider phone (just digits):")
  provider["phone"] = input().strip()
  if not re.search("^[2-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$", provider["phone"]):
    print("Invalid phone. Discarding and continuing with what we have so far.")
    break
  providers.append(provider)
  print("Ok, provider added to list of providers. Moving on to next.\n")

print(str(providers))
