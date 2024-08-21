import tkinter as tk
from tkinter import colorchooser

def change_bg_color():
    color_code = colorchooser.askcolor(title="Choose background color")
    if color_code[1]:
        root.config(bg=color_code[1])


root = tk.Tk()
root.title("Change Background Color")


btn = tk.Button(root, text="Choose Background Color", command=change_bg_color)
btn.pack(pady=20)

root.geometry("400x300")
root.mainloop()