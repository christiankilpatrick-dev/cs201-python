#week 5 Chapter 5 A

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
        print("Enter a name: (blank to quit)")
        name = input()
        if name == '':
            break

        if name in birthdays:
            print(birthdays[name] + " is the birthday of " + name)
        else:
            print('I do not have birthday information for ' + name)
            print('What is their birthday?')
            bday = input()
            birthdays[name] = bday
            print('Birthday database updated.')

for i in birthdays.keys():
    print(i)

for l in birthdays.values():
    print(l)

for k in birthdays.items():
    print(k)

print(list(birthdays.items()))

for k, v in birthdays.items():
    print("Key: " + k + " Value: " + str(v))
