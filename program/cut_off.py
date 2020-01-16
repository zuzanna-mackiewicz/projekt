import numpy as np
from tkinter import *
import tkinter.messagebox
import tkinter as tk

window = Tk()
window.geometry('300x300')
window.title('SET UP CUT_OFF VALUE:')

label_1 = Label(window, text = 'Look for:').place(x = 5, y = 5)

entry1 = tk.IntVar()
option1 = tk.BooleanVar()
option2 = tk.BooleanVar()
option3 = tk.BooleanVar()

def cut_off():
    print(entry1.get())
    print(option1.get())
    print(option2.get())
    print(option3.get())

def close():
    exit()

option_1 = Checkbutton(window, text = 'strong interactions (distance <= 3)', variable = option1).place(x = 10, y = 30)
option_2 = Checkbutton(window, text = 'medium interactions (3 < distance <= 7)', variable = option2).place(x = 10, y = 60)
option_3 = Checkbutton(window, text = 'weak interactions (7 < distance <= 10)', variable = option3).place(x = 10, y = 90)

label_2 = Label(window, text = 'Set up your own cut-off value:').place(x = 5, y = 130)

entry_1 = Entry(window, width = 3, textvariable =entry1).place(x= 10, y = 160)
label_3 = Label(window, text = 'Å').place(x = 30, y = 160)

button_1 = Button(window, width = 7, text = 'Apply', command = cut_off).place(x = 5, y = 200)
button_2 = Button(window, width = 7, text = 'Close', command = close).place(x = 5, y = 230)

window.mainloop()


    # window = Tk()
    # window.geometry('300x300')
    # window.title('SET UP CUT_OFF VALUE:')
    #
    # label_1 = Label(window, text = 'Look for:').place(x = 5, y = 5)
    #
    # option_1 = Checkbutton(window, text = 'strong interactions (distance <= 3)').place(x = 10, y = 30)
    # option_2 = Checkbutton(window, text = 'medium interactions (3 < distance <= 7)').place(x = 10, y = 60)
    # option_3 = Checkbutton(window, text = 'weak interactions (7 < distance <= 10)').place(x = 10, y = 90)
    #
    # label_2 = Label (window, text = 'Set up your own cut-off value:').place(x = 5, y = 130)
    #
    # entry_1 = Entry(window).place(x= 10, y = 160)
    #
    # button_1 = Button(window, text = 'Apply', command = chosen_value).place(x = 5, y = 200)
    #
    # window.mainloop()

cut_off()