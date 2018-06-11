min_val = 10
max_val = 1000

# for i in range(min_val, max_val + 1):
#    if i % 5 == 0 and not i % 2 == 0:
#        print(str(i) + " is an odd multiple of 5")

# for i in range(min_val, max_val + 1):
#    if i % 3 == 0 or i % 10 == 0:
#        print(str(i) + " is either a multiple of 3 or 10 (or both)")

for i in range(min_val, max_val + 1):
    if i % 2 != 0:
        print(str(i) + " is odd")
