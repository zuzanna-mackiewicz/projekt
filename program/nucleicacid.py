from Bio.PDB.PDBParser import PDBParser
from tkinter import filedialog
import os

def nucleic_acid_reader():

    path = os.getcwd()

    nucleic_acid_path_string = filedialog.askopenfilename(initialdir = 'path',title = "SELECT NUCLEIC ACID STRUCTURE:",filetypes = (("PDB files","*.pdb"),("all files","*.*")))
    nucleic_acid_name = os.path.basename(nucleic_acid_path_string)

    with open(nucleic_acid_path_string, 'r') as nucleic_acid:

        parser = PDBParser(PERMISSIVE=1)
        nucleic_acid_structure = parser.get_structure(nucleic_acid_name, nucleic_acid)
        model_structure = nucleic_acid_structure[0]

    list_of_nucleotides = ['A', 'C', 'G', 'T', 'U']

    for chain in model_structure:
        for residue in chain:
            residue_name = residue.get_resname().strip()
            if residue_name in list_of_nucleotides:
                print(residue_name, str(residue.get_id()[1]))

    return residue_name, str(residue.get_id()[1])

nucleic_acid_reader()