
from __future__ import print_function

import httplib2
import os
import idea_date

from apiclient import discovery
from oauth2client import tools
from oauth2client import client
from oauth2client.file import Storage

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def _get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    try:
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_known_args()[0]
    except ImportError:
        flags = None
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def _get_service_connection(spreadsheet_id):
    credentials = _get_credentials()
    http = credentials.authorize(httplib2.Http())
    discovery_url = ('https://sheets.googleapis.com/$discovery/rest?version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discovery_url)
    return service


def setup_sheet(spreadsheet_id):
    service = _get_service_connection(spreadsheet_id)
    body = {
      'values': [['Date', 'Idea']]
    }
    result = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, range='DefaultBank!A1:B1',
        valueInputOption='RAW', body=body).execute()


def write_idea(timestamp, idea_string, spreadsheet_id):
    service = _get_service_connection(spreadsheet_id)

    body = {
      'values': [[timestamp, idea_string]]
    }
    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id, range='DefaultBank!A2:B2',
        valueInputOption='RAW', body=body).execute()


def read_ideas(spreadsheet_id):
    '''
    Returns a list of ideas (date, idea)
    '''
    service = _get_service_connection(spreadsheet_id)

    rangeName = 'DefaultBank!A2:B'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=rangeName).execute()
    values = result.get('values', [])
    idea_list = [(idea_date.parse_date(d), idea) for [d, idea] in values]
    return idea_list


if __name__ == '__main__':
    write_idea('2017-01-01', 'the first idea of the year')
    read_ideas()
