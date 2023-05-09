import pandas as pd
import json

def make_csv_from_metadata(path):
    file_ = open(path, 'r')
    data = json.loads(file_.read())
    file_names, labels, splits, originals = [], [], [], []
    for key, val in data.items():
        file_names.append(key)
        labels.append(val['label'])
        splits.append(val['split'])
        originals.append(val['original'])
    csv = pd.DataFrame({
        'file_name': file_names,
        'labels': labels,
        'splits': splits,
        'originals': originals
    })
    return csv

if __name__ == '__main__':
    make_csv_from_metadata()