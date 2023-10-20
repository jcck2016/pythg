
print("please use............")
print("'f' or 'F' for Fahrenheit")
print("'c' or 'C' for Celsius")
print("'k' or 'K' for Kelvin")
unit = input("what is the temperature unit you are using ?   ")
temp = input("what is the temperature of the water?  ")

if unit == "f" or unit == "F":
    if int(temp) == 212:
        print("water is boiling at 212 F")
    else:
        print("water is not boiling , must hit 212 F")

elif unit == "c" or unit == "C":
    if int(temp) == 100:
        print("water is boiling at 100 C")
    else:
        print("water is not boiling , must hit 100 C")

elif unit == "k" or unit == "K":
    if int(temp) == 373:
        print("water is boiling at 373 K")
    else:
        print("water is not boiling , must hit 373 K")

else:
    print("invalid unit entered ....you have to enter either 'f','c' or'k'")
