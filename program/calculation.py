import pandas as pd

def calculations(target_data, ligands_data, cut_off):
    '''
        Calculates distances between each atom form target structure and each atom from ligands structures.
        Selects only those target-ligand pairs that are close to each other within previously selected distance.
        Prints list of interaction present between molecules.

        :param target_data: list of amino acids/nucleotides from the target structure with their coordinates
        :type target_data: list of lists
        :param ligands_data: list of atoms from ligands structures with their coordinates
        :type ligands_data: list of lists
        :param cut_off: minimal and maximal distance for contacts search
        :type cut_off: list
        :return: table with ligands and amino acids/nucleotides close to each other within the selected distance
        :rtype: data frame
        '''

    df_target = pd.DataFrame.from_records(target_data)
    df_target.columns = ['symbol', 'number', 'x', 'y', 'z']
    df_ligands = pd.DataFrame.from_records(ligands_data)
    df_ligands.columns = ['symbol', 'number', 'x', 'y', 'z', 'ligand']

    df_target['n'] = 1
    df_ligands['n'] = 1

    merged_data = pd.merge(df_target, df_ligands, on='n', how='outer')

    merged_data['distance'] = ((merged_data['x_x'] - merged_data['x_y']) ** 2 + (
                merged_data['y_x'] - merged_data['y_y']) ** 2 + (merged_data['z_x'] - merged_data['z_y']) ** 2) ** (0.5)

    if cut_off[2] == 0 and cut_off[3] == 0:
        filtered_data = merged_data[(merged_data.distance > cut_off[0]) & (merged_data.distance <= cut_off[1])].drop(
            columns=['x_x', 'x_y', 'y_x', 'y_y', 'z_x', 'z_y', 'n'])
    else:
        filtered_data = merged_data[((merged_data.distance > cut_off[0]) & (merged_data.distance <= cut_off[3])) | (
                    (merged_data.distance > cut_off[3]) & (merged_data.distance <= cut_off[2]))].drop(
            columns=['x_x', 'x_y', 'y_x', 'y_y', 'z_x', 'z_y', 'n'])

    filtered_data = filtered_data[['symbol_x', 'number_x', 'ligand']].drop_duplicates()
    listed_data = filtered_data.values.tolist()

    if cut_off[1] == 3:
        print(f'For selected cut-off value (0-3 A) interaction between:')
    elif cut_off[1] == 7 and cut_off[0] == 3:
        print(f'For selected cut-off value (3-7 A) interaction between:')
    elif cut_off[1] == 10 and cut_off[0] == 7:
        print(f'For selected cut-off value (7-10 A) interaction between:')
    else:
        print(f'For selected cut-off value ({cut_off[1]} A) interaction between:')

    for i in range(0, len(listed_data)):
        print(f'{listed_data[i][0]} {listed_data[i][1]} and ligand {listed_data[i][2]}')

    return filtered_data

if __name__ == '__main__':
    calculations()