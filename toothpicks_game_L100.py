
print("welcome to the 13 toothpicks game !!!!!!!!!!!!")
print("*******************************************")
play1_name = input("enter play1's name: ")
play2_name = input("enter play2's name: ")

picks_left = 13

while True:
    print("| " * picks_left)
    print("There are still", picks_left, "toothpicks left")
    p1_move = int(
        input("{play1_name} how many toothpicks are you removing ? "))
    picks_left -= p1_move
    if picks_left <= 0:
        print("there are no mpre picks left........")
        print(f"{play1_name} WON the game !")
        break

    print("| " * picks_left)
    print("There are still", picks_left, "toothpicks left")
    p2_move = int(
        input("{play2_name} how many toothpicks are you removing ? "))
    picks_left -= p2_move

    print("| " * picks_left)
    print("There are still", picks_left, "toothpicks left")
    if picks_left <= 0:
        print("there are no mpre picks left........")
        print(f"{play2_name} WON the game!")
        break
