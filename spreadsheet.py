class Spreadsheet(object):
    def __init__(self, spreadsheet_id, sheet_name):
        self._spreadsheet_id = spreadsheet_id
        self._sheet_name = sheet_name

    @property
    def spreadsheet_id(self):
        return self._spreadsheet_id

    @property
    def sheet_name(self):
        return self._sheet_name


def extract_spreadsheet_id(spreadsheet_url):
    return spreadsheet_url.split('/d/')[1].split('/')[0]


def setup_spreadsheet():
    spreadsheet_url = raw_input('''Please create an empty google spreadsheet which will contain your ideas and enter the URL: ''')
    spreadsheet_id = extract_spreadsheet_id(spreadsheet_url)
    sheet_name = raw_input('''Please enter the name of the sheet ('tab name' in the bottom of the document) [defaults to 'Sheet1']: ''') or 'Sheet1'
    return Spreadsheet(spreadsheet_id, sheet_name)

