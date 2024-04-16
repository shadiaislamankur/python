cars=["Ford","Volvo","BMW"]
car1="Ford"
car2="Volvo"
car3="BMW"

x=cars[0]
cars[0]="Toyota"

x=len(cars)

for x in cars:
    print(x)

cars.append("Honda")
for x in cars:
    print(x)

cars.pop(1)
#cars.remove("Volvo")