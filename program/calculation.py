import pandas as pd

def calculations(target_data, ligands_data, cut_off):

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

    for i in range(0, len(listed_data)):
        if cut_off[1] == 3:
            print(f'For selected cut-off value (0-3 Å): interaction between {listed_data[i][0]} {listed_data[i][1]} and ligand {listed_data[i][2]}')
        elif cut_off[1] == 7 and cut_off[0] == 3:
            print(f'For selected cut-off value (3-7 Å): interaction between {listed_data[i][0]} {listed_data[i][1]} and ligand {listed_data[i][2]}')
        elif cut_off[1] == 10 and cut_off[0] == 7:
            print(f'For selected cut-off value (Å): interaction between {listed_data[i][0]} {listed_data[i][1]} and ligand {listed_data[i][2]}')
        else:
            print(f'For selected cut-off value ({cut_off[1]} Å): interaction between {listed_data[i][0]} {listed_data[i][1]} and ligand {listed_data[i][2]}')

    return filtered_data

if __name__ == '__main__':
    calculations()