from tkinter import filedialog
import os
from biopandas.mol2 import PandasMol2
from biopandas.mol2 import split_multimol2
from pandas import DataFrame
#

def ligands_reader():

    path = os.getcwd()

    ligands_path_string = filedialog.askopenfilename(initialdir = 'path',title = "SELECT LIGANDS STRUCTURE:",filetypes = (("MOL2 files","*.mol2"),("all files","*.*")))
    ligands_name = os.path.basename(ligands_path_string)

    ligands_data = []
    model_number = 1
    with open(ligands_path_string, 'r') as ligands:
        for ligand in split_multimol2(ligands_path_string):
            pmol = PandasMol2().read_mol2_from_list(mol2_lines=ligand[1], mol2_code=ligand[0])
            atom_coord = pmol.df[['atom_name', 'atom_id', 'x', 'y', 'z']]

            atom_coord['model_number'] = model_number
            model_number += 1

            df = DataFrame(atom_coord, columns=['atom_name', 'atom_id', 'x', 'y', 'z', 'model_number'])
            model_data = df.values.tolist()
            ligands_data = ligands_data + model_data

    print(ligands_data)
    return ligands_data

ligands_reader()