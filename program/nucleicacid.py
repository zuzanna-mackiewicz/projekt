from Bio.PDB.PDBParser import PDBParser
from tkinter import filedialog
from tkinter import *
import os

def nucleic_acid_reader():
    '''
    Parses selected PBD file with DNA/RNA structure using BioPython module.
    Lists all nucleotides in structure with their coordinates.

    :return: symbols, numbers and coordinates of nucleotides
    :rtype: list of lists
    '''

    window = Tk()
    path = os.path.normpath(os.getcwd() + os.sep + os.pardir)
    path = os.path.join(path, 'files')

    nucleic_acid_path_string = filedialog.askopenfilename(initialdir = 'path',title = "SELECT NUCLEIC ACID STRUCTURE:",filetypes = (("PDB files","*.pdb"),("all files","*.*")))
    nucleic_acid_name = os.path.basename(nucleic_acid_path_string)
    window.destroy()

    with open(nucleic_acid_path_string, 'r') as nucleic_acid:

        parser = PDBParser(PERMISSIVE=1)
        nucleic_acid_structure = parser.get_structure(nucleic_acid_name, nucleic_acid)
        model_structure = nucleic_acid_structure[0]

    list_of_nucleotides = ['A', 'C', 'G', 'T', 'U']

    nucleic_acid_data = []
    for chain in model_structure:
        for residue in chain:
            residue_name = residue.get_resname().strip()
            if residue_name in list_of_nucleotides:
                for atom in residue:
                    atom_data = []
                    atom_data.append(residue_name)
                    atom_data.append(str(residue.get_id()[1]))
                    atom_data.append(atom.get_vector()[0])
                    atom_data.append(atom.get_vector()[1])
                    atom_data.append(atom.get_vector()[2])

                    nucleic_acid_data.append(atom_data)

    # print(nucleic_acid_data)
    return nucleic_acid_data, nucleic_acid_name[6:-4]

if __name__ == '__main__':
    nucleic_acid_reader()
