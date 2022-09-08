print("How many volunteers do you have?")
try:
  num_volunteers = int(input())
except:
  print("Oops, you didn't enter an integer")
  exit()

total = 0
for v in range(0, num_volunteers):
  print("Enter the number of bird sightings from volunteer #"+str(v+1))
  try:
    volunteer_report = int(input())
    if (volunteer_report < 0):
      raise
    total = total + volunteer_report
  except:
    print("Oops, you didn't enter a positive integer")
    exit()

print("Total number of sightings: "+str(total))
