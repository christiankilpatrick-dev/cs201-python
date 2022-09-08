def compute_new_office(current_office):
    office = current_office.split(' ')
    if len(office)== 2 and current_office.isupper()==True and len(office[0]) == 3 and len(office[1]) == 4:
        new_number = int(office[1]) + 1000
        new_office = office[0] + ' ' + str(new_number)
        return new_office


    else:
        return current_office