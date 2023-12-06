
import pandas as pd
import json
def read_file(file_path, output_type=''):

    if output_type == 'dataframe':
        return pd.read_csv(file_path, delimiter='\t', skip_blank_lines=False)

    else:
        with open(file_path, 'r') as file:
            # return file.readlines()
            return [x.strip() for x in file.readlines()]

def read_json(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)

    return data