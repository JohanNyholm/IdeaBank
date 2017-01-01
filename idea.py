
import remote_sheet
from oauth2client import tools


def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    """https://docs.google.com/spreadsheets/d/1yHpDejkJ-znUIRmvNA4Z64fJPpBo29Kl11Z3WRpD3rA/edit?usp=sharing"""
    try:
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None

    print(flags)


if __name__ == '__main__':
    main()
