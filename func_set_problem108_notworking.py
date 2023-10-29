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


print(is_even(4566778))
print(slugify(" i love YOU New YoRK    ! "))
print(count_vowels("dsdeadtgtysregght"))
print(slugify_predef_sep("hello world CkR  !   ! !!", "***"))
print(slugify_predef_sep("hello world CkR  !   ! !!"))
