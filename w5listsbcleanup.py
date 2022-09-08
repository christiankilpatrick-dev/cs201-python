#w4 lists b revised
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
total = sum(reports)
min_so_far = min(reports)
max_so_far = max(reports)
average = total/len(reports)


# output the results
print("Total number of sightings: "+str(total))
print("Average number of sightings: "+str(total / num_volunteers))
print("Min number of sightings: "+str(min_so_far))
print("Max number of sightings: "+str(max_so_far))
