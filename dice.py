import random

dice_count = input("input the number of dice you wish to roll with: ")
side_count = input("input the number of sides each die will have:  ")

# dice_count_num = int(dice_count)
# side_count_num = int(side_count)

roll = input(
    "begin to roll !! .... please hit any character to roll and hit 'q' to quite :  ")

# THE roll the dice loop
while roll != "q":
    print("****You have selected", dice_count,
          "dice each with ", side_count, "sides *****")

    # The number of dice loop
    divided_result = "|"
    for dice in range(int(dice_count)):
        roll_result = random.randint(1, int(side_count))
        divided_result += f"{roll_result}|"
    print(divided_result)

    # print("****The roll result of a single roll is ", roll_result)
    roll = input(
        "begin to roll !! .... please hit any character to roll OR hit 'q' to quite :  ")


# eye1 = random.randint(1, 6)

# roll_result = random.randint(1, side_count)
