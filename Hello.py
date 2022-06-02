import tkinter as tk

window = tk.Tk()
window.title("Hello")

label = tk.Label(window,text="Hello tkinter!")
window.geometry('300x200')
label.pack()

box1 = tk.Label(
    window,
    text="Colour 1",
    bg="blue",
    fg="white"
)
box1.pack(
    ipadx=10,
    ipady=10
)
box1 = tk.Label(
    window,
    text="Colour 2",
    bg="red",
    fg="white"
)
box1.pack(
    ipadx=10,
    ipady=10
)
box1 = tk.Label(
    window,
    text="Colour 1",
    bg="yellow",
    fg="white"
)
box1.pack(
    ipadx=10,
    ipady=10
)

window.mainloop()


 