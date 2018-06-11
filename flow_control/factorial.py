value = 10
print("Calculating the factorial of " + str(value))

charlie = 1
for i in range(1, value + 1):
    charlie = charlie * i

print(str(value) + "! = " + str(charlie))
