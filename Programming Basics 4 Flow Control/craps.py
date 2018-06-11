import random

point_set = False
point = 0
break_loop = False

while not break_loop:
    die_one = random.randint(1, 6)
    die_two = random.randint(1, 6)
    die_sum = die_one + die_two
    print("I rolled " + str(die_sum))
    if not point_set:
        if die_sum in (2, 3, 12):
            print("Craps!")
            break_loop = True
        elif die_sum in (7, 11):
            print("Winner!")
            break_loop = True
        else:
            print("The point is " + str(die_sum))
            point = die_sum
            point_set = True
    else:
        if die_sum == point:
            print("Winner!")
            break_loop = True
        elif die_sum == 7:
            print("Craps!")
            break_loop = True
