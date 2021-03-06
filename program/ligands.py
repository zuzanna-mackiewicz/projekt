from tkinter import filedialog
from tkinter import *
import os
from biopandas.mol2 import PandasMol2
from biopandas.mol2 import split_multimol2
from pandas import DataFrame


def ligands_reader():
    '''
    Parses selected MOL2 file with structures of previously docked ligands using BioPandas module.
    Lists all atoms from all ligands with their coordinates.

    :return: symbols, numbers and coordinates of atoms + number of atom
    :rtype: list of lists
    '''

    window = Tk()
    path = os.path.normpath(os.getcwd() + os.sep + os.pardir)
    path = os.path.join(path, 'files')

    ligands_path_string = filedialog.askopenfilename(initialdir = 'path',title = "SELECT LIGANDS STRUCTURE:",filetypes = (("MOL2 files","*.mol2"),("all files","*.*")))
    ligands_name = os.path.basename(ligands_path_string)
    window.destroy()


    ligands_data = []
    model_number = 1
    with open(ligands_path_string, 'r') as ligands:
        for ligand in split_multimol2(ligands_path_string):
            pmol = PandasMol2().read_mol2_from_list(mol2_lines=ligand[1], mol2_code=ligand[0])
            atom_coord = pmol.df[['atom_name', 'atom_id', 'x', 'y', 'z']]

            atom_coord = atom_coord.assign(column=model_number)
            model_number += 1

            model_data = atom_coord.values.tolist()
            ligands_data = ligands_data + model_data

    # print(ligands_data)
    return ligands_data

if __name__ == '__main__':
    ligands_reader()