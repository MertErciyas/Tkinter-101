from random import choice
import tkinter

bomb = tkinter.Tk()
bomb.title('Bomb')

def randomColor():
    hexadecimal = ["#"+''.join([choice('ABCDEF0123456789') for i in range(6)])]
    return hexadecimal

size = 50
for i in range(6,0,-1):
    bomb.geometry(f'{size}x{size}')
    size += 50
    print(i) 
    bomb.configure(bg=randomColor()) if i != 6 else bomb.configure(bg='white')
    bomb.after(2000, bomb.update())
bomb.destroy()

bomb.mainloop()
print('BOOM!')