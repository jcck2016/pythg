print("welcome to the 13 toothpicks game !!!!!!!!!!!!")
print("*******************************************")
play1_name = input("enter play1's name: ")
play2_name = input("enter play2's name: ")

picks_left = 13
current_player = play1_name

while True:
    print("| " * picks_left)
    print("There are still", picks_left, "toothpicks left")
    p1_move = int(
        input(f"{current_player} how many toothpicks are you removing ? "))
    picks_left -= p1_move
    if picks_left <= 0:
    print("there are no more picks left........")
    print(f"{current_player} WON the game !")
    break

if current_player == play1_name:
    current_player = play2_name
else:
    current_player = play1_name


print(".......GAME OVER ..............")

"""
    print("| " * picks_left)
    print("There are still", picks_left, "toothpicks left")
    if picks_left <= 0:
        print("there are no more picks left........")
        print(f"{play2_name} WON the game!")
        break
"""
