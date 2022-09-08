#W5 Combining Collections A


cars = [
  {"buyer": "Jane Edwards", "price":6000, "make":"Honda"},
  {"buyer": "Ahmed Moustef", "price":9000, "make":"Honda"},
  {"buyer": "Mike McGinney", "price":2000, "make":"Ford"},
  {"buyer": "Jeffrey Pouch", "price":4000, "make":"Honda"},
  {"buyer": "Beatrice Duff", "price":6000, "make":"GM"}
]

total = 0
subtotal_by_make = {}

for car in cars:
  price = car.get("price", 0)
  total = total + price
  make = car.get("make", "")
  subtotal_by_make[make] = subtotal_by_make.get(make, 0) + price

print("Total was $"+str(total))
for make in subtotal_by_make.keys():
  subtotal = subtotal_by_make.get("price", 0)
  print(make+" subtotal: $"+str(subtotal))

for i in cars:
    car_buyer= i.get("buyer", 0)
    print(car_buyer)



#could not figure this out. i.e. adding subtotals of makes???
