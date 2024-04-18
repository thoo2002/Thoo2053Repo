from car import Car
with open("cars.txt") as file:
    carlist=[]
    for line in file:
        inputs = line.strip()
        tokens = inputs.split()
        gas = int(tokens[2])
        miles = int(tokens[3])
        newcar=Car(tokens[0],tokens[1],gas,miles)
        carlist.append(newcar)
    print(carlist[1].get_gas_tank())
    carlist[1].drive()
    print(carlist[1].get_gas_tank())
    print(carlist[1].get_odometer())
        