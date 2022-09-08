#W6Bvalidation 1
#program below reads in the provider's name, address, zip code, and phone number
#from a block of text
providers = []
try:
  while True:
    provider = {}
    print("Provider name (just hit Enter if done entering providers):")
    provider["name"] = input().replace('"', '').strip()
    if len(provider["name"]) == 0:
      break

    print("Provider address (just hit Enter if done entering providers):")
    provider["address"] = input().replace('"', '').strip()
    if len(provider["address"]) == 0:
      break

    print("Provider zip code:")
    provider["zip"] = int(input().strip())
    if provider["zip"] > 99999 or provider["zip"] <= 0:
      print("Invalid zip. Discarding and continuing with what we have so far.")
      break
    
    print("Provider phone:")
    provider["phone"] = int(input().strip())
    if provider["phone"] > 9999999999 or provider["phone"] < 1000000000:
      print("Invalid phone. Discarding and continuing with what we have so far.")
      break

    providers.append(provider)
    print("Ok, provider added to list of providers. Moving on to next.\n")
except:
  print("Invalid input encountered, moving on to rest of the program")

print(str(providers))
