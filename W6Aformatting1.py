# W5Aformatting1

my_data = {
  "C-12":{
    "name":"Carbon 12\n",
    "mass":12.0,
    "half_life":-1
  },
  "C-14":{
    "name":"Carbon 14\n",
    "mass":14.003241,
    "half_life":5730
  }
}

for symbol in my_data.keys():  # iterate over the dictionary's keys
  next_item = my_data[symbol]
  symbol = symbol.replace('-', '') # remove hyphens
  name = next_item['name'].strip() # remove leading and trailing whitespace
  mass = next_item['mass']
  half_life = next_item['half_life']
  if half_life > 0:
    half_life_info = (f'half life of {half_life:,} years')   # reformat the half_life variable
  else:
    half_life_info = f'no half life (is not radioactive)'
  print(f"{name} ({symbol}): {half_life:.4f} g/mol, {half_life_info}.")
  # format the mass with 4 positions after the decimal, please
