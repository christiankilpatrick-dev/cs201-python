#W6 Summary Lecture

import re

info = [
    {"name": "Joey", "phone": "503-888-5689"},
    {"name": "Mahatma", "phone": "541-888-5689"},
    {"name": "Artie", "phone": "567-888-5689"},
    {"name": "Rachael", "phone": "254-888-5689"},
    {"name": "Mike", "phone": "754544-888-5689"},
    {"name": "Padma", "phone": "652-888-5689"},
    {"name": "Smith", "phone": "541-888-5689"}
    ]



nrecs = len(info)
num_valid = 0
num_in_oregon = 0

for record in info:
    phone = record["phone"]
    if re.search("^[0-9]{3}-[0-9]{3}-[0-9]{4}$", phone):
        num_valid = num_valid + 1
        print(phone)
        hyphen_loc = phone.find("-")
        area_code = phone[0:hyphen_loc]
        if area_code == "503" or area_code == "541" or area_code == "971":
            num_in_oregon = num_in_oregon + 1

percent_in_oregon = 100.0*num_in_oregon/num_valid
print(f'{percent_in_oregon:.2f}% are in Oregon')
