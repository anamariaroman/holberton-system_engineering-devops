#!/usr/bin/python3
""" Python script that, using this REST API for a given employee ID
returns information about his/her TODO list progress. """

import requests
import sys


if __name__ == '__main__':
    """ Function that returns information about employed ID """
    user_ID = sys.argv[1]
    employee = requests.get('https://jsonplaceholder.typicode.com/users/' +
                            user_ID).json()

    todo = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + user_ID).json()
    complete_tasks = [task for task in todo if task.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get('name'), len(complete_tasks), len(todo)))

    for task in todo:
        if task.get('completed') is True:
            print("\t {}".format(task.get('title')))
