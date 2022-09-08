# read in the bird reports of the volunteers
reports = []
print("How many volunteers do you have?")
try:
  num_volunteers = int(input())
  if (num_volunteers < 1):
      raise
  for v in range(0, num_volunteers):
    print("Enter the number of bird sightings from volunteer #"+str(v+1))
    volunteer_report = int(input())
    if (volunteer_report < 0):
      raise
    reports.append(volunteer_report)
except:
  print("Oops, you didn't enter a positive integer")
  exit()

# compute the statistics
total = 0
min_so_far = -1
max_so_far = -1
for i in reports:
  total = total + i
  if (min_so_far == -1 or i < min_so_far):
    min_so_far = i
  if (max_so_far == -1 or i > max_so_far):
    max_so_far = i

# output the results
print("Total number of sightings: "+str(total))
print("Average number of sightings: "+str(total / num_volunteers))
print("Min number of sightings: "+str(min_so_far))
print("Max number of sightings: "+str(max_so_far))
