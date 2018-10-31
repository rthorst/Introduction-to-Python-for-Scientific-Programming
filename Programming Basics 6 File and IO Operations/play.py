filename = "filename.txt"
with open(filename, "a") as file:
    text = input("give me a line to write:")
    file.write(text)

