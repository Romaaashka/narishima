
fuelCapacity = int(input(" fuel capacity = "))
fuelAmount = int(input(" Fuel amount = "))

alarm_thershould = fuelCapacity / 10

if fuelAmount < alarm_thershould:
    print( "Red light, Fuel amount ")

else:
    print( "Green light ")
