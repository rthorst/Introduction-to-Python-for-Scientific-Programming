value = 10000
print("printing hailstone sequence from " + str(value))

while True:
    print(str(int(value)))
    if value == 1:
        break
    elif value % 2 == 0:
        value = value / 2
    else:
        value = 3 * value + 1
