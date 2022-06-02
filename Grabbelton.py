import tkinter as tk
from tkinter import Label, ttk
import random

grabbelton = tk.Tk()
grabbelton.title("Grabbelton")
grabbelton.geometry('500x400')
grabbelton.resizable(False, False)

toys = ["Pokemon Cards","Plushie","Nintendo 3DS","Lego","Boardgames","Jumping Rope","Sketch Book","Nintendo Switch","Bubble Gum","Chewing Gum"]

def randomToy():
    randomToy = random.choice(toys)
    toys.remove(randomToy)
    return randomToy

def btn1():
    if len(toys) == 0:
        print("There is nothing left.")
    else:
        toyGot = randomToy()
        print(f"Congratulations! You got: {toyGot}")
        label = Label(grabbelton, text=toyGot)
        label.pack()

grabbelton_button = ttk.Button(
    grabbelton,
    text='Press me!',
    command=btn1
)
grabbelton_button.pack(
    ipadx=20,
    ipady=20,
    expand=True
)


grabbelton.mainloop()