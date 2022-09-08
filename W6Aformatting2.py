#W6Aformatting 2 

#Wikipedia writes the half-life of Carbon 14 as "5,730 ± 40 years".
#Maybe we want to break this into two variables, half_life and error_bounds

## See 'Formatting module for more complicatedd version


half_life_info = "5,730 ± 40 years"
print(half_life_info)

# split on the spaces
half_life_parts = half_life_info.split(' ')
print("half life parts: "+str(half_life_parts))

# take chunk 0
# and remove the commas
# and convert to an integer
half_life = int(half_life_parts[0].replace(",",""))
print("half life is " + str(half_life))

# take string from chunk 2 (numbering from 0)
# and convert to an integer
error_bounds = int(half_life_parts[2])
print("error bounds are "+str(error_bounds))






