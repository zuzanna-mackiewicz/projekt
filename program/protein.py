from Bio.PDB.PDBParser import PDBParser
from tkinter import filedialog
from tkinter import *
import os

def protein_reader():
    '''
    Parses selected PBD file with protein structure using BioPython module.
    Lists all amino acids in structure with their coordinates.

    :return: symbols, numbers and coordinates of amino acids
    :rtype: list of lists
    '''

    window = Tk()
    path = os.path.normpath(os.getcwd() + os.sep + os.pardir)
    path = os.path.join(path, 'files')

    protein_path_string = filedialog.askopenfilename(initialdir = 'path',title = "SELECT PROTEIN STRUCTURE:",filetypes = (("PDB files","*.pdb"),("all files","*.*")))
    protein_name = os.path.basename(protein_path_string)
    window.destroy()


    with open(protein_path_string, 'r') as protein:

        parser = PDBParser(PERMISSIVE=1)
        protein_structure = parser.get_structure(protein_name, protein)
        model_structure = protein_structure[0]

    list_of_aminoacids = ['ALA', 'ASX', 'CYS', 'ASP', 'GLU', 'PHE', 'GLY', 'HIS', 'ILE', 'LYS', 'LEU', 'MET', 'ASN', 'PRO', 'GLN',
              'ARG', 'SER', 'THR', 'SEC', 'VAL', 'TRP', 'XAA', 'TYR', 'GLX', 'PYL', 'UNK', 'XLE', 'MSE', 'ME0']

    protein_data = []
    for chain in model_structure:
        for aminoacid in chain:
            aminoacid_name = aminoacid.get_resname().strip()
            if aminoacid_name in list_of_aminoacids:
                for atom in aminoacid:
                    atom_data = []
                    atom_data.append(aminoacid_name)
                    atom_data.append(str(aminoacid.get_id()[1]))
                    atom_data.append(atom.get_vector()[0])
                    atom_data.append(atom.get_vector()[1])
                    atom_data.append(atom.get_vector()[2])


                    protein_data.append(atom_data)

    # print(protein_data)
    return protein_data, protein_name[9:-4]

if __name__ == '__main__':
    protein_reader()