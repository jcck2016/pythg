# defining this veriable in the GLOBAL scope, video 112
animal = "Zebra"


def outter_func():
    print("we are seeing this animal inside of a function 'outter' as --- ", animal)

    def inner_func():
        print("we are seeing this animal inside of a function 'inner' that is inside of function 'outter' as --- ", animal)
    inner_func()

# defining this veriable in the LOCAL (LEXICAL) scope, video 113


def zoo():
    animal = "Polar Bear"
    print("we are seeing this animal inside of function 'zoo' --- ", animal)


# calling function in video 112
outter_func()
print("we are seeing this animal outside of any function as --- ", animal)

# calling function in video 113
zoo()
