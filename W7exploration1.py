#Week 7 exploration 1 A

def load_reports(file_name):
  """
  Loads the volunteers' reports, one per line from the file
  """
  volunteer_reports = []
  data_file = open(file_name)
  for line in data_file:
    line = line.strip()
    if len(line) > 0:
      sighting = int(line)
      if (sighting < 0):
        raise print('Each sighting should be a positive integer')
      volunteer_reports.append(sighting)
  return volunteer_reports
  
reports = load_reports('data.txt')
print(f'Total number of sightings: {len(reports)}')
if len(reports) > 0:
  print(f'Average number of sightings: {sum(reports)/len(reports):.2f}')
  print(f'Min number of sightings: {min(reports)}')
  print(f'Max number of sightings: {max(reports)}')
