#!/usr/bin/python3
"""gather data from an api"""

import csv
import requests
import sys

if __name__ == "__main__":

    userId = str(sys.argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    filename = userId + '.csv'
    with open(filename, 'w') as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            if task.get('userId') == int(userId):
                csv_writer.writerow([userId, user.get('username'),
                                    str(task.get('completed')),
                                    task.get('title')])
