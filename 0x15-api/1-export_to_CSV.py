#!/usr/bin/python3
"""gather data from an api"""

import csv
import requests
import sys

if __name__ == "__main__":

    id = str(sys.argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(id)).json()
    uname = user.get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    filename = id + '.csv'
    with open(filename, 'w') as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            if task.get('userId') == int(id):
                csv_writer.writerow([id, uname, task.get('completed'),
                                 task.get('title')])
