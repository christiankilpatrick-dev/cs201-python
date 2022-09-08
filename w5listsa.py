print("How many volunteers do you have?")
try:
  num_volunteers = int(input())
except:
  print("Oops, you didn't enter an integer")
  exit()

total = 0
min_so_far = -1
max_so_far = -1
for v in range(0, num_volunteers):
  print("Enter the number of bird sightings from volunteer #"+str(v+1))
  try:
    volunteer_report = int(input())
    if (volunteer_report < 0):
      raise
    if (min_so_far == -1 or volunteer_report < min_so_far):
      min_so_far = volunteer_report
    if (max_so_far == -1 or volunteer_report > max_so_far):
      max_so_far = volunteer_report
    total = total + volunteer_report
  except:
    print("Oops, you didn't enter a positive integer")
    exit()

print("Total number of sightings: "+str(total))
if (num_volunteers > 0):
  print("Average number of sightings: "+str(total / num_volunteers))
  print("Min number of sightings: "+str(min_so_far))
  print("Max number of sightings: "+str(max_so_far))
