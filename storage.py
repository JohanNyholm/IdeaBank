import pickle
import os

STORAGE_FILE = ".storage.pkl"

def get_storage_file():
    d = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(d, STORAGE_FILE)


def write_spreadsheet_id(spreadsheet_id):
    with open(get_storage_file(), 'wb') as pkl_file:
        pickle.dump(spreadsheet_id, pkl_file)


def read_spreadsheet_id():
    try:
        with open(get_storage_file(), 'rb') as pkl_file:
            return pickle.load(pkl_file)
    except IOError:
        return None
