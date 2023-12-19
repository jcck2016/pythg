# It's race day and our starting grid is set! Charles sits on pole and Lando brings up the rear.
drivers = ["Charles", "Pierre", "Valterri", "Lewis", "George","Lando"]

# Oh dear, we've misspelled "Valtteri" as "Valterri".  Update the drivers list to include the correct spelling!

drivers[2] = 'Valtteri'
print("This the list after the spell error was corected for Valtteri: " ,drivers)
print("----------------------------------------------------------------------\n")
# Esteban makes it out of the pits and joins the pack just in time.  Add "Esteban" to the end of the drivers list!

drivers.append('Esteban')
print("This the list after 'Esteban' was added : " ,drivers)
print("----------------------------------------------------------------------\n")

# What's this? There's another group of drivers that comes out of nowhere to join the race! Add each element from the others list to the end of the drivers list.
others = ["Blue", "Elton", "Colt"]
drivers.extend(others)

print("This the list after the 'others' list was added: " ,drivers)
print("----------------------------------------------------------------------\n")

# Colt looks lost out there! He has a horrible fiery crash.  Remove the last element from the drivers list ("Colt")

drivers.pop()
print("This the list after the driver 'Colt' was removed: " ,drivers)
print("----------------------------------------------------------------------\n")

# Oh dear, there's a huge crash at the front! Remove the first element from the driver's list
drivers.pop(0)
print("This the list after the first driver was removed: " ,drivers)
print("----------------------------------------------------------------------\n")

# And again the leader of the pack runs into trouble! He's not out of the race, but he's now moved to last place.  Remove the first driver in the list, store it in variable, and then add it to the end of the list.
first= drivers[0]
print("This the first driver was removed: " ,first)
drivers.pop(0)
drivers.append(first)
print("This the list after the former driver was appended to the last place: " ,drivers)
print("----------------------------------------------------------------------\n")


# My idiotic cat, Blue, is in the middle of the pack.  Delete "Blue" from the drivers list using the remove method!
drivers.remove("Blue")
print("This the list after the  driver 'Blue' was removed: " ,drivers)
print("----------------------------------------------------------------------\n")


# My dog, Elton, is making a remarkable charge up the leadboard! Remove Elton from his current position in the list and insert him at index 2.

drivers.remove("Elton")
drivers.insert(1,"Elton")
print("This the list after the  driver 'Elton' became the 2nd place: " ,drivers)
print("----------------------------------------------------------------------\n")

# The race is over! It's time for the podium ceremony.  Create a new list called podium that contains the first 3 elements from the drivers list. (use a slice!)
prize_places = drivers[0:3:1]
print("This the list of 3 finalists that would win the trophy !!: " , prize_places)
print("----------------------------------------------------------------------\n")


# Loop over the drivers list and print out a leadboard that includes a driver's finishing position and their name, like this:
# 1. Valtteri
# 2. Lewis
# 3. Elton
# 4. George
# 5. Lando
# 6. Esteban
# 7. Pierre

print("Here is an overall leader board and their names !! .... \n")
i = -1
while i < len(drivers) +1:
    i += 1
    print(i+1,". ",drivers[i])
    