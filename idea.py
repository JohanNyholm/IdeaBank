#!/usr/bin/python2

from __future__ import print_function
import remote_sheet

import argparse
import datetime
import idea_date
import idea_date


def prepare_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('idea_string', nargs='?')
    parser.add_argument('--list', help='list ideas', action='store_true')
    return parser


def parse_args():
    parser = prepare_parser()
    args = parser.parse_args()
    return args


def print_ideas(idea_list):
    for i, (d, idea_string) in enumerate(idea_list):
        print('%i: %s, %s' % (i, idea_date.date_to_string(d),
                              idea_string))
        # print(idea_date.date_to_string(idea_date), idea_string)


def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    """https://docs.google.com/spreadsheets/d/1yHpDejkJ-znUIRmvNA4Z64fJPpBo29Kl11Z3WRpD3rA/edit?usp=sharing"""
    args = parse_args()
    if args.list:
        idea_list = remote_sheet.read_ideas()
        print_ideas(idea_list)
    elif args.idea_string:
        time_stamp = idea_date.date_to_string(datetime.datetime.today())
        idea_string = args.idea_string
        remote_sheet.write_idea(time_stamp, idea_string)


if __name__ == '__main__':
    main()
