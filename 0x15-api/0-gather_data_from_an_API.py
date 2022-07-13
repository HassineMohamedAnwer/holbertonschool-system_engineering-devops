#!/usr/bin/python3
"""gather data from
an api"""

import requests
import sys

if __name__ == "__main__":

    completed = 0
    totalTasks = 0
    tasksTitles = []
    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId)).json()

    name = user.get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos/').json()

    for task in todos:
        if task.get('userId') == int(userId):
            if task.get('completed'):
                tasksTitles.append(task['title'])
                completed += 1
            totalTasks += 1
    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

    for i in tasksTitles:
        print("\t {}".format(i))
