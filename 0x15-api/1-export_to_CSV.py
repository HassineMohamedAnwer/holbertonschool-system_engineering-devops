#!/usr/bin/python3
"""gather data from an api"""

import requests
import sys

if __name__ == "__main__":

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId)).json()

    name = user.get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos/').json()

    with open('{}.csv'.format(userId), 'w') as f:

        for task in todos:
            f.write('"{}","{}","{}","{}"\n'
                    .format(user.get('id'), user.get('username'),
                            task.get('completed'), task.get('title')))
