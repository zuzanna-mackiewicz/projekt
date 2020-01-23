from tkinter import *
import tkinter as tk
import numpy as np
import pandas as pd
import os
import pathlib
import csv

from nucleicacid import nucleic_acid_reader
from protein import protein_reader
from ligands import ligands_reader
from cut_off import distance
from calculation import calculations

target_data = []
ligands_data = []
cut_off = []

window1 = Tk()
window1.geometry('200x150')
window1.title('')

label_1 = Label(window1, text = 'Chose type of interactions:').place(x=25, y=5)

mode = tk.StringVar()

def get_structure():

    global target_data
    global ligands_data

    if mode.get() == 'protein':
        window1.destroy()
        target_data = protein_reader()
    elif mode.get() == 'DNA/RNA':
        window1.destroy()
        target_data = nucleic_acid_reader()

    ligands_data = ligands_reader()

def close():
    exit()

mode_1 = Radiobutton(window1, text='protein - ligand', width=19, indicatoron=0, variable=mode, value='protein', command=get_structure).place(x=25, y=30)
mode_2 = Radiobutton(window1, text='RNA/DNA - ligand', width=19, indicatoron=0, variable=mode, value='DNA/RNA', command=get_structure).place(x=25, y=60)

button_1 = Button(window1, width=7, text='Close', command=close).place(x=68, y=110)

window1.mainloop()

window2 = Tk()
window2.geometry('300x300')
window2.title('SET UP CUT_OFF VALUE:')

label_2 = Label(window2, text='Look for:').place(x=5, y=5)

entry1 = tk.IntVar()
option1 = tk.BooleanVar()
option2 = tk.BooleanVar()
option3 = tk.BooleanVar()

def get_distances():

    global cut_off
    cut_off = distance(entry1.get(), option1.get(), option2.get(), option3.get())
    if cut_off[1] != 0:
        window2.destroy()

option_1 = Checkbutton(window2, text='strong interactions (distance 0-3 Å)', variable=option1).place(x=10, y=30)
option_2 = Checkbutton(window2, text='medium interactions (distance 3-7 Å)', variable=option2).place(x=10, y=60)
option_3 = Checkbutton(window2, text='weak interactions (distance 7-10 Å)', variable=option3).place(x=10, y=90)

label_3 = Label(window2, text='Set up your own cut-off value:').place(x=5, y=130)

entry_1 = Entry(window2, width=3, textvariable=entry1).place(x=10, y=160)
label_4 = Label(window2, text='Å').place(x=30, y=160)

button_2 = Button(window2, width=7, text='Apply', command=get_distances).place(x=5, y=200)
button_3 = Button(window2, width=7, text='Close', command=close).place(x=5, y=230)

window2.mainloop()

def calc_data():

    result = calculations(target_data, ligands_data, cut_off)
    result['nucleotide/aminoacid'] = result['symbol_x'] + result['number_x']
    interactions = result[['nucleotide/aminoacid', 'ligand']].reset_index()

    sorted_result = result['ligand'].value_counts().reset_index()
    sorted_result = sorted_result.rename(columns={'index': 'ligand', 'ligand': 'count'})
    print(sorted_result)

    path = (pathlib.Path.cwd()/ "..").resolve()
    path = path / 'results'
    path.mkdir(parents=True, exist_ok=True)

    interactions.to_csv(path/'target-ligands interactions', index = False, sep=',', header=True)
    sorted_result.to_csv(path/'ligands activity', index = False, sep=',', header=True)

calc_data()