import tkinter as tk
import random
    
def roll_dice():
    dice_value = random.randint(1, 6)
    dice_label.config(text=str(dice_value))

root = tk.Tk()
root.geometry("200x200")
root.title("Dice Simulator")

dice_label = tk.Label(root, text="", font=("Helvetica", 72))
dice_label.pack()

roll_button = tk.Button(root, text="Roll Dice", command=roll_dice)
roll_button.pack()

root.mainloop()
