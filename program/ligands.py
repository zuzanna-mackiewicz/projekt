from Bio.PDB.PDBParser import PDBParser
from tkinter import filedialog
import os

def ligands_reader():

    path = os.getcwd()

    ligands_path_string = filedialog.askopenfilename(initialdir = 'path',title = "SELECT LIGANDS STRUCTURE:",filetypes = (("PDB files","*.pdb"),("all files","*.*")))
    ligands_name = os.path.basename(ligands_path_string)
    print(ligands_name)

    with open(ligands_path_string, 'r') as ligands:

        parser = PDBParser(PERMISSIVE=1)
        ligands_structure = parser.get_structure(ligands_name, ligands)


    print(path)
    print(ligands_path_string)
    print(ligands_structure)

    return ligands_structure

ligands_reader()