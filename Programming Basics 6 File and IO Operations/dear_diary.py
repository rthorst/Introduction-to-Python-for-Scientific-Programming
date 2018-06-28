import datetime

start_entry = "Dear Diary,\r\n\t"

with open("diary.txt", "a") as diary_file:
    while True:
        print("Write an entry in your diary.")
        print()
        text = input(start_entry)
        if text == "quit":
            break
        to_write = start_entry + text
        diary_file.write(str(datetime.date.today()) + "\r\n")
        diary_file.write("---------------\r\n")
        diary_file.write(to_write + "\r\n\r\n")
