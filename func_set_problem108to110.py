# a function that tells a number is an even number
def is_even(num):
    return num % 2 == 0

# write a function that put a string into lower case and remove leading and trailing spaces


def slugify(words):
    return words.lower().strip().replace(" ", "-")


def slugify_predef_sep(words11, sep="-"):
    return words11.lower().strip().replace(" ", sep)


def count_vowels(words2):
    vcount = 0
    for char in words2:
        if char in "aeiou":
            vcount += 1
    return vcount


def divide2(x1=1, y1=4):
    return x1/y1

# we can have as many as pre def parameters as we want but have to come AFTER the first required parameter when the function is called, video 110


def greet(person, msg1="welcome", msg2="how are you", msg3="have a great day"):
    print(f"Hi {person}..{msg1} ...{msg2}...{msg3} ... !!!")

# named argument parameter where the order of the parameter DOESNT MATTER !


def get_total(price, qty=1, tax=0.09, discount=0):
    subtotal = price * qty * (1 - discount)
    return subtotal * (1 + tax)


print(is_even(4566778))
print(slugify(" i love YOU New YoRK    ! "))
print(count_vowels("dsdeadtgtysregght"))
print(slugify_predef_sep("hello world CkR  !   ! !!", "***"))
print(slugify_predef_sep("hello world CkR  !   ! !!"))


print(divide2(8, 3))

# video 110
print(greet("tony"))


# video 111
print(get_total(9.75, 5, 0.01, 0.5))
print(get_total(price=9.75, qty=5, tax=0.01, discount=0.5))
print(get_total(price=9.75, tax=0.01, discount=0.5, qty=5))

print(get_total(price=20.95))
print(get_total(price=20.95, tax=0.09))
