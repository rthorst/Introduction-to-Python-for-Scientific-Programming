import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

save_path = filedialog.asksaveasfilename(initialdir = ".", title = "Your title goes here")
print(save_path)
