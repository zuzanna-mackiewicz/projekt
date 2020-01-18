from tkinter import *
import tkinter as tk
import numpy as np
import pandas as pd

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

    ligands_data = [['CL', 7, -6.8042, -3.8904, -0.5599, 19], ['C', 1, -5.1126, -3.2734, -1.0689, 20], ['C', 2, -3.9361, -2.5265, -1.0269, 20], ['C', 3, -3.2837, -2.195, -2.2156, 20], ['C', 4, -3.8098, -2.6113, -3.4393, 20], ['C', 5, -4.9876, -3.359, -3.4771, 20], ['C', 6, -5.6412, -3.6913, -2.2895, 20], ['CL', 7, -5.9177, -3.6825, 0.396, 20], ['C', 1, -5.1332, -3.2349, -2.7596, 21], ['C', 2, -5.7942, -4.4159, -3.0954, 21], ['C', 3, -6.5804, -5.0627, -2.1407, 21], ['C', 4, -6.7022, -4.5278, -0.8576, 21], ['C', 5, -6.0387, -3.3456, -0.5267, 21], ['C', 6, -5.2517, -2.6963, -1.479, 21], ['BR', 7, -4.0678, -2.3569, -4.0514, 21], ['C', 1, -5.4702, -3.4361, -1.3988, 22], ['C', 2, -4.5277, -2.853, -0.5526, 22], ['C', 3, -3.3825, -2.267, -1.0938, 22], ['C', 4, -3.1845, -2.2664, -2.4751, 22], ['C', 5, -4.1306, -2.8513, -3.3177, 22], ['C', 6, -5.277, -3.4381, -2.7797, 22], ['BR', 7, -7.0224, -4.2303, -0.6678, 22], ['C', 1, -5.1365, -3.2039, -2.6311, 23], ['C', 2, -5.8734, -4.3561, -2.9023, 23], ['C', 3, -6.6166, -4.9561, -1.8847, 23], ['C', 4, -6.62, -4.4033, -0.6034, 23], ['C', 5, -5.8808, -3.25, -0.3371, 23], ['C', 6, -5.1365, -2.6476, -1.3526, 23], ['BR', 7, -4.1291, -2.3894, -4.0082, 23], ['C', 1, -5.4881, -3.4182, -1.3958, 24], ['C', 2, -5.3106, -3.4041, -2.7787, 24], ['C', 3, -4.1691, -2.8134, -3.3225, 24], ['C', 4, -3.2121, -2.2405, -2.4839, 24], ['C', 5, -3.3944, -2.2573, -1.1005, 24], ['C', 6, -4.5349, -2.8472, -0.5534, 24], ['BR', 7, -7.0337, -4.218, -0.6569, 24], ['C', 1, -5.91, -4.3739, -2.5539, 25], ['C', 2, -5.2047, -3.5759, -3.4539, 25], ['C', 3, -4.388, -2.5506, -2.9748, 25], ['C', 4, -4.28, -2.3277, -1.6016, 25], ['C', 5, -4.9879, -3.1291, -0.705, 25], ['C', 6, -5.8055, -4.1553, -1.1808, 25], ['BR', 7, -7.0168, -5.7636, -3.2007, 25], ['C', 1, -3.5161, -2.533, -1.5929, 26], ['C', 2, -3.4652, -2.1867, -2.9435, 26], ['C', 3, -4.4146, -2.7043, -3.8265, 26], ['C', 4, -5.4087, -3.5639, -3.3587, 26], ['C', 5, -5.4561, -3.9078, -2.0075, 26], ['C', 6, -4.5087, -3.3924, -1.1211, 26], ['I', 7, -2.1039, -1.7637, -0.2754, 26], ['C', 1, -5.3256, -3.3892, -2.3335, 27], ['C', 2, -6.0389, -4.5317, -2.6973, 27], ['C', 3, -6.8625, -5.1602, -1.7616, 27], ['C', 4, -6.9704, -4.6467, -0.469, 27], ['C', 5, -6.2554, -3.504, -0.1091, 27], ['C', 6, -5.4307, -2.8725, -1.0418, 27], ['I', 7, -4.0984, -2.4509, -3.7247, 27], ['C', 1, -5.2825, -3.3164, -2.3757, 28], ['C', 2, -5.993, -4.4866, -2.6444, 28], ['C', 3, -6.7461, -5.0862, -1.6333, 28], ['C', 4, -6.7867, -4.5163, -0.3607, 28], ['C', 5, -6.0748, -3.3461, -0.0961, 28], ['C', 6, -5.3205, -2.7433, -1.1042, 28], ['I', 7, -4.1603, -2.421, -3.8793, 28], ['C', 1, -5.3251, -3.3809, -2.3394, 29], ['C', 2, -6.0276, -4.5313, -2.6991, 29], ['C', 3, -6.8465, -5.1633, -1.7615, 29], ['C', 4, -6.9604, -4.6453, -0.4713, 29], ['C', 5, -6.2562, -3.4947, -0.1155, 29], ['C', 6, -5.4363, -2.8596, -1.05, 29], ['I', 7, -4.1049, -2.4374, -3.7333, 29], ['C', 1, -4.3255, -2.507, -1.7504, 30], ['C', 2, -5.5108, -2.8709, -1.1108, 30], ['C', 3, -5.5637, -2.8991, 0.284, 30], ['C', 4, -4.4354, -2.5645, 1.0331, 30], ['C', 5, -3.2521, -2.2012, 0.3897, 30], ['C', 6, -3.1949, -2.1718, -1.0049, 30], ['I', 7, -4.2436, -2.464, -3.8272, 30], ['C', 1, -4.9482, -3.0857, -0.9623, 31], ['C', 2, -3.7144, -2.4187, -1.0433, 31], ['C', 3, -3.1039, -2.1829, -2.2778, 31], ['C', 4, -3.7188, -2.6116, -3.4528, 31], ['C', 5, -4.9428, -3.2757, -3.3935, 31], ['C', 6, -5.5512, -3.5103, -2.1578, 31], ['C', 7, -5.6108, -3.3399, 0.3787, 31], ['O', 8, -6.7487, -3.9084, 0.3655, 31], ['O', 9, -4.98, -2.9657, 1.4181, 31], ['C', 1, -4.9418, -3.0901, -0.9584, 32], ['C', 2, -3.7105, -2.4185, -1.0377, 32], ['C', 3, -3.1027, -2.174, -2.2719, 32], ['C', 4, -3.718, -2.5983, -3.4482, 32], ['C', 5, -4.9396, -3.267, -3.3906, 32], ['C', 6, -5.5453, -3.5103, -2.1552, 32], ['C', 7, -5.6014, -3.3538, 0.3823, 32], ['O', 8, -6.7323, -3.9361, 0.3683, 32], ['O', 9, -4.9754, -2.973, 1.4222, 32], ['C', 1, -5.5591, -3.457, -1.3009, 33], ['C', 2, -5.45, -3.5354, -2.6993, 33], ['C', 3, -4.3564, -2.979, -3.3678, 33], ['C', 4, -3.3531, -2.3342, -2.6468, 33], ['C', 5, -3.4433, -2.2453, -1.2587, 33], ['C', 6, -4.5378, -2.8025, -0.5926, 33], ['C', 7, -6.7464, -4.0628, -0.5761, 33], ['O', 8, -7.6245, -4.6469, -1.2876, 33], ['O', 9, -6.7771, -3.942, 0.6898, 33], ['C', 1, -5.1078, -3.1874, -0.9615, 34], ['C', 2, -3.897, -2.4751, -0.9752, 34], ['C', 3, -3.2339, -2.2068, -2.1755, 34], ['C', 4, -3.7722, -2.6478, -3.383, 34], ['C', 5, -4.9723, -3.3567, -3.3904, 34], ['C', 6, -5.6335, -3.6237, -2.1889, 34], ['C', 7, -5.8276, -3.4769, 0.3424, 34], ['O', 8, -5.2386, -3.1386, 1.4181, 34], ['O', 9, -6.9671, -4.0369, 0.2646, 34]]

    if mode.get() == 'protein':
        window1.destroy()
        target_data = protein_reader()
    elif mode.get() == 'DNA/RNA':
        window1.destroy()
        target_data = nucleic_acid_reader()

    # ligands_data = ligands_reader()

    # return target_data

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
    # return cut_off

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
    print(result)

    sorted_result = result['ligand'].value_counts()

    print(sorted_result)

calc_data()