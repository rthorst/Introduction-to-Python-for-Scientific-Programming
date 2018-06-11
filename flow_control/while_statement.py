import random as rdm

while True:
    die_one = rdm.randint(1, 6)
    die_two = rdm.randint(1, 6)
    die_sum = die_one + die_two
    print("the sum is " + str(die_sum))
    if die_sum == 2:
        print("snake-eyes!")
        break
