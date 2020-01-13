from Bio.PDB.PDBParser import PDBParser
from tkinter import filedialog
import os
import csv

def nucleic_acid_reader():

    path = os.getcwd()

    nucleic_acid_path_string = filedialog.askopenfilename(initialdir = 'path',title = "SELECT NUCLEIC ACID STRUCTURE:",filetypes = (("PDB files","*.pdb"),("all files","*.*")))
    nucleic_acid_name = nucleic_acid_path_string[-8:]
    # print(nucleic_acid_name)

    with open(nucleic_acid_path_string, 'r') as nucleic_acid:

        parser = PDBParser(PERMISSIVE=1)
        nucleic_acid_structure = parser.get_structure(nucleic_acid_name, nucleic_acid)
        model_structure = nucleic_acid_structure[0]

    # print(path)
    # print(nucleic_acid_path_string)
    # print(nucleic_acid_structure)
    # print(model_structure)

    return model_structure

nucleic_acid_reader()