import pickle
import os

STORAGE_FILE = ".storage.pkl"

def get_storage_file():
    home_dir = os.path.expanduser('~')
    return os.path.join(home_dir, STORAGE_FILE)


def write_spreadsheet_id(spreadsheet_id):
    with open(get_storage_file(), 'wb') as pkl_file:
        pickle.dump(spreadsheet_id, pkl_file)


def read_spreadsheet_id():
    try:
        with open(get_storage_file(), 'rb') as pkl_file:
            return pickle.load(pkl_file)
    except IOError:
        return None
