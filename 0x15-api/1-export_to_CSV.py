#!/usr/bin/python3
"""gather data from an api"""

import requests
import sys
import csv

if __name__ == "__main__":

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    with open('{}.csv'.format(userId), 'w') as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            if task.get('userId') == int(userId):
                csv_writer.writerow([userId, user.get('username'), str(task.get('completed')),
                                 task.get('title')])
