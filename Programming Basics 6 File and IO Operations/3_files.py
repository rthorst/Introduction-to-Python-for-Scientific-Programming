with open("filenamehere.txt", "a+") as open_file:
    current_text = open_file.read()
    open_file.write("text to \r\n")

# this is identical to

open_file = open("filenamehere.txt", "a+")
current_text = open_file.read()
open_file.write("text to write\r\n")
open_file.close()

# use the first one!  that way you don't have to remember to close

# a, r, w and c are all valid file modes
# as are a+, r+, w+ and c+
# append "b" to a file mode to make it binary
