bottles = 99

print("*****************************")
print("There are ", bottles, " bottle(s) of beer on the wall")

bottles = int(bottles)
for x in range(bottles, 0, -1):
    print("*****************************")
    print(f"There are {x} bottle(s) of beer on the wall")
    if x == 1:
        print(f"Take one down, pass it around.....There are no more bottles of beer remain on the wall")
    else:
        print(
            f"Take one down, pass it around.....There are now {x - 1} bottle(s) remain on the wall")


# try to do the above using WHILE loop again ............ tomorrow

print("\n")
print ("++++++++++++++++++++++++++++++++++++++++++++++")
print ("now we are doing 200 bottles using while loop")

bottles2 = 200

while bottles2 > 0:
    print(f"Take one down, pass it around.....There are {bottles2} bottles of beer remain on the wall")
    
    if bottles2 == 1:
        print(f"Take one down, pass it around.....There are no more bottles of beer remain on the wall")
    else:
        print(
            f"Take one down, pass it around.....There are now {bottles2-1} bottle(s) remain on the wall")
    print("*" *50)
    bottles2 -= 1