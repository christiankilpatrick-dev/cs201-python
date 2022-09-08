#W5 Dictionaries A



counts_by_make= {}
while True:
  print("Enter a car manufacturer (or blank line to end)")
  make = input()
  if (len(make) == 0):
    break
  counts_by_make[make] = counts_by_make.get(make, 0) + 1

for make in sorted(counts_by_make.keys()):
  counts = counts_by_make.get(make, 0)
  if (counts >= 2):
    print(make+" was mentioned "+str(counts)+" times") 
