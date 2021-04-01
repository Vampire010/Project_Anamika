from random import random, seed, randint, gauss

print(len("Ananmika"))
print(bin(15))
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
print(hex(5))

val1 = max(20, 24, 12, 13, 16, 18)
print(val1)

val2 = min(20, 24, 12, 13, 16, 18)
print(val2)


def gen_random():

    return randint(10,20)


print(gen_random())
print(gauss(10,15))