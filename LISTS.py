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
