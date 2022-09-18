from logging import root
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import ImageGrab
from PIL import Image

root = ThemedTk(theme="black")
root.title("Digit Recognizer -- Srivatsa")



def getter():
    x=root.winfo_rootx()
    y=root.winfo_rooty()
    x1=x+canvas.winfo_width()
    y1=y+canvas.winfo_height()
    print(x,y,x1,y1)
    # im = ImageGrab.grab().crop((x,y,x1,y1))
    im = ImageGrab.grab()
    im.show()
    
def clear_all():
    canvas.delete('all')

def draw_lines( event):
        x = event.x
        y = event.y
        r=15
        canvas.create_oval(x-r,y-r, x + r, y + r, fill='white' , outline = 'white')
        
canvas = tk.Canvas(root, width=700, height=500, cursor="cross"  , bg = 'black')
canvas.pack()


clear_btn = ttk.Button(root, text="clear", command=clear_all)
clear_btn.pack()

show_btn = ttk.Button(root, text="Show", command= getter)
show_btn.pack()

canvas.bind('<B1-Motion>', draw_lines)
ttk.Label(text = "jasijdajlsdasjdas as;dlkasda;s d").pack()

root.configure(bg='gray')
root.mainloop()