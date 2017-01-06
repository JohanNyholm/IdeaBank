import datetime
import dateutil.parser as DP

DATE_FORMAT = '%Y-%m-%d %H:%M'


def parse_date(date_string):
    return datetime.datetime.strptime(date_string, DATE_FORMAT)


def date_to_string(datetime_object):
    return datetime_object.strftime(DATE_FORMAT)
