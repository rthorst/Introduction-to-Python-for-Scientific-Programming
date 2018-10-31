import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

save_path = filedialog.asksaveasfilename(initialdir = ".", title = "File to overwrite")
print(save_path)
with open(save_path, "w") as save_file:
    save_file.writelines(input("What to write?:"))
