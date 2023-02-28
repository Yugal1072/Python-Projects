import tkinter as tk
import random

def roll_dice():
    dice_value = random.randint(1, 6)
    label1.config(text=str(dice_value))

root = tk.Tk()
root.geometry('250x250')
root.title('Dice Simulator')

label1 = tk.Label(root, text="", font=("Helvetica 70 bold"))
label1.pack()

button = tk.Button(root, text="Roll Dice", command=roll_dice )
button.pack()

root.mainloop()