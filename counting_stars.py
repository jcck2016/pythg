count = input("enter number of STARS for the base of your star pyramid: ")
count_down = int(count)
count_up = count_down - 1

print("-----------This is your pyramid looks like upside down: ")
while count_down > 0:
    print("*" * count_down)
    count_down -= 1


count_down = int(count)
print(count_down)
print(count_up)
print("-----------This is your pyramid looks like right side up: ")
diff = count_down - count_up

while diff < count_down:
    print("*" * diff)
    diff += 1
