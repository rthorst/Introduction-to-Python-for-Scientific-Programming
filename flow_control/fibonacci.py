first_int = 1
second_int = 1
max_val = 1000

print("Printing the Fibonacci sequence up to " + str(max_val))
print(str(first_int))
while second_int <= max_val:
    print(str(second_int))
    int_sum = first_int + second_int
    first_int = second_int
    second_int = int_sum


