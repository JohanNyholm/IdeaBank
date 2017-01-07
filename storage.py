import pickle
import os

STORAGE_FILE = ".idea_bank_storage.pkl"


def get_storage_file():
    home_dir = os.path.expanduser('~')
    return os.path.join(home_dir, STORAGE_FILE)


def write_spreadsheet(sheet):
    with open(get_storage_file(), 'wb') as pkl_file:
        pickle.dump(sheet, pkl_file)


def read_spreadsheet():
    try:
        with open(get_storage_file(), 'rb') as pkl_file:
            return pickle.load(pkl_file)
    except IOError:
        return None
