# Week 7 Exploration 2B (CSVs)


import csv
def load_reports():
  """
  Returns a list of bird report counts from USGS sample data.
  """
  data_file = open("sample1.txt")
  csv_reader = csv.reader(data_file)
  next(csv_reader) # skip header row

  reports = []
  for row in csv_reader:
    if (len(row) == 6):
      route = row[2]
      species_total = row[5].strip()
      if (route == "001"):
        reports.append(int(species_total))
  return reports

reports = load_reports()
print(f'Average species reports per year: {sum(reports)/len(reports):.2f}')
