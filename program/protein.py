from Bio.PDB.PDBParser import PDBParser
from tkinter import filedialog
import os

def protein_reader():

    path = os.getcwd()

    protein_path_string = filedialog.askopenfilename(initialdir = 'path',title = "SELECT PROTEIN STRUCTURE:",filetypes = (("PDB files","*.pdb"),("all files","*.*")))
    protein_name = os.path.basename(protein_path_string)

    with open(protein_path_string, 'r') as protein:

        parser = PDBParser(PERMISSIVE=1)
        protein_structure = parser.get_structure(protein_name, protein)
        model_structure = protein_structure[0]

    list_of_aminoacids = ['ALA', 'ASX', 'CYS', 'ASP', 'GLU', 'PHE', 'GLY', 'HIS', 'ILE', 'LYS', 'LEU', 'MET', 'ASN', 'PRO', 'GLN',
              'ARG', 'SER', 'THR', 'SEC', 'VAL', 'TRP', 'XAA', 'TYR', 'GLX', 'PYL', 'UNK', 'XLE', 'MSE', 'ME0']

    for chain in model_structure:
        for aminoacid in chain:
            aminoacid_name = aminoacid.get_resname().strip()
            if aminoacid_name in list_of_aminoacids:
                print(aminoacid_name, str(aminoacid.get_id()[1]))

    return aminoacid_name, str(aminoacid.get_id()[1])

protein_reader()