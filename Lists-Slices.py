waitlist = ['Juan', 'Jack', 'Harvey', 'Woody', 'Martin']
print(f"waitlist now: ", waitlist)

# expand a list using the append function
waitlist.append('Jennifer')
print(f"waitlist added: ", waitlist)
print("*"*80)
# expand a list using the extend function ... difference is accept an iterable (each character or item) and append them each separately to the end of the list
waitlist.extend('VILLAGEPEOPLE')
print(f"waitlist added again: ", waitlist)
print("*"*80)
# more useful example is you add another list into the existing list
more_people = ['Mary', 'Joe', 'Don', 'Jason', 'Timmy', 'Ashma', 'Lebron']
waitlist.extend(more_people)
print(f"waitlist added by another group of people: ", waitlist)
print("*"*80)
# insert function into a list
num = [7, 9, 10, 11, 12]
num.insert(1, 8)
print(num)
print("*"*80)
print("*"*80)

# slices of list
# list [begin, end , step]  end does not include the last element  --
print("superduper"[3:7])
# print slice with a step number of 2 ... every second letter off that range ...
print("superduper"[3:7:2])
print("*"*80)
print("*"*80)

# replacing some values within a slice that is part of a list ...
num = [4, 5, 6, 7, 8, 9]
print(num[1:3])
num[1:3] = ["cat", "mouse"]
print(num[1:3])
print(num)
# expanding the value within a slice range that is part of a list ...
num = [4, 5, 6, 7, 8, 9, 10]
print(num[1:3])
num[1:3] = ["cat", "mouse", "sheep", "cow", "pig", "duck", "spider", "Mussel"]
print(num)
print("*"*80)
print("*"*80)
# method that clear out a list..
num = [4, 5, 6, 7, 8, 9, 10]
print(f"number list before clear method", num)
num.clear()
print(f"number list after clear method", num)

num = [4, 5, 6, 7, 8, 9, 10]
print(f"number list before remove method: ", num)
num.remove(7)
print(f"number list afer remove method rid of (1st occurance of ) 7: ", num)

num = [4, 5, 6, 7, 8, 9, 10]
print(f"number list before pop method: ", num)
print(f"the item removed by the pop method: ", num.pop())
print(f"number list after pop (last item removed) method: ", num)
print(num.pop())
print(f"number list after 'another' pop (last item removed) method: ", num)

num = [4, 5, 6, 7, 8, 9, 10]
print(f"We now reset the number list before pop (this time with indexed position) method: ", num)
print(f"we popped the index position 3 which is : ", num.pop(3))
print(f"now it looks like this: ", num)
print("*"*80)
print("*"*80)

num = [4, 5, 6, 7, 8, 9, 10]
print(f" we have a list of [4,5,6,7,8,9,10], with slice of [2:] ..", num[2:])
del num[2:]
print(f" what if we delete the slice of [2:] .. the result is: ", num)
