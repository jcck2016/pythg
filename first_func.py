
def laugh20():
    print("*" * 20)
    print("HeHeHeHe!!..." * 10)
    print("HaHahaHa!!..." * 10)
    print("*" * 20)


def laugh_how(intensity):
    print("*" * 100)
    print("HeHeHeHe!!..." * intensity)
    print("HaHahaHa!!..." * intensity)
    print("*" * 100)


def divide_me(numerator, denominator):
    print("*" * 100)
    print("we are dividing ...........")
    print(numerator / denominator)


def divide_me_return_me(numerator, denominator):
    print("*" * 100)
    print("we are dividing ... and returning ...........")
    print(numerator / denominator)
    return numerator/denominator


laugh20()

user_input = input(f"enter the intensity of your laugh:  ")
user_input = int(user_input)

laugh_how(user_input)

user_numerator = input(f"enter the top number of division:  ")
user_denominator = input(f"enter the bottom number of division: ")

user_numerator = int(user_numerator)
user_denominator = int(user_denominator)

divide_me(user_numerator, user_denominator)
