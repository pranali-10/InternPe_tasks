from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title('Digital Clock')
root.configure(background="black")

def time():
    day_string = strftime("%A")
    day_label.config(text = day_string)

    time_string = strftime('%H:%M:%S %p')
    time_label.config(text=time_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    time_label.after(1000, time)

day_label = Label(root, font=("ds-digital", 35), background="black", foreground="magenta")
day_label.pack()

time_label = Label(root, font=("ds-digital", 45), background="black", foreground="magenta")
time_label.pack()

date_label = Label(root, font=("ds-digital", 35), background="black", foreground="magenta")
date_label.pack()
time()
mainloop()
