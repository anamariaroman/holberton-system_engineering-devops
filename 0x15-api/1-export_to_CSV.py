#!/usr/bin/python3
""" Using what you did in the task #0, extend your Python
script to export data in the CSV format. """

import csv
import requests
import sys


if __name__ == '__main__':
    """ Function that writes and exports all data in the csv format """
    user_ID = sys.argv[1]
    employee = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         user_ID).json()
    employee_name = employee.get('username')

    todo = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + user_ID).json()

    with open('{}.csv'.format(user_ID), mode='w') as cvs_file:
        tasks_writer = csv.writer(cvs_file, quoting=csv.QUOTE_ALL)
        for task in todo:
            tasks_writer.writerow([user_ID, employee_name,
                                 task.get('completed'), task.get('title')])
