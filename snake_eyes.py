import random
eye1 = random.randint(1, 6)
eye2 = random.randint(1, 6)
count = 0

while eye1 != 1 or eye2 != 1:
    eye1 = random.randint(1, 6)
    eye2 = random.randint(1, 6)
    count += 1
    print(f"{eye1} - {eye2}")
    print("*******This ran ", count, " times*********")

print("Finally !!!!! ............")
print("SNAKE EYES O__O !!!!! ............")
print(f"{eye1} - {eye2}")
print("*******This ran ", count, " times*********")
