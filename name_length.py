
fname = input("what is your fist name?  ")
lname = input("what is your last name?  ")
print("your name is: ", fname, lname)
name_length = len(fname) + len(lname)
print("your name has total length of: ", name_length)

if name_length == 12:
    print("*"*50)
    print(f"{fname} {lname} is EXACTLY average length ! ")

elif name_length < 12:
    print("*"*50)
    print(f"{fname} {lname} is SHORTER than average length !")

else:
    print("*"*50)
    print(f"{fname} {lname} is LONGER than average length !")
