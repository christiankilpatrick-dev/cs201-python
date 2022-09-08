#Week 8 Exploration 4A

import os

os.chdir("C:\\CS201")

import re
import operator

SALARY_FILE = "salary-data.txt"

def load_employees():
    #Returns the list of allemployees, each has a name and list of jobs.
    #[
    #   {"name": "Al Albertson", "jobs" : [
    #       {"org": "Biology", "pct":80, "salary":75000},
    #       {"org": "Chemistry", "pct":20, "salary": 76000}
    #   ]},
    #   {"name": "Beto Banana", "jobs" : [
    #       {"org": "Maintenance", "pct":100, "salary":55000}
    #   ]}, ...
    # ]

    with open(SALARY_FILE, "r") as myfile:
        text = myfile.read().replace('\n', '~')

    result = list()
    all_employee_texts = text.split('-----------------------------------')

    for employee_text in all_employee_texts:
        pieces = employee_text.split('Job Org: ')

        employee = dict()

        #grab the employee's name from the first piece
        m = re.search('~Name: +(.+)~~', pieces[0])
        if m:
            employee['name'] = m.group(1)

        employee['jobs'] = list()

        #grab the employee's jobs from the following pieces
        for piece in pieces[1:]:
            job = dict()

            #print('>'+piece)
            m = re.search('(.+)~FTE%: +(\d+\.\d+)~.+\$(\d+\.\d+)~', piece)
            if m:
                job['org'] = m.group(1)
                job['pct'] = float(m.group(2))
                job['salary'] = float(m.group(3))
                # print (str(job))

            employee['jobs'].append(job)

        result.append(employee)
    return result

employees = load_employees()
CAUTION = "\nADAPTED from public-use data published by Oregon State University\nSalary figures were randomly adjusted"
print(CAUTION)

totals_by_org = {}
for employee in employees:
    for job in employee['jobs']:
        annual_cost = job['pct'] * 0.01 * job['salary']
        group = job['org']
        totals_by_org[group] = totals_by_org.get(group, 0) + annual_cost

for group in totals_by_org.keys():
    annual_cost = totals_by_org[group]
    if annual_cost > 5E6:
        print('${:,.2f}'.format(annual_cost)+ '\t' + group)

print(CAUTION)
