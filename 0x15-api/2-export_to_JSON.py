#!/usr/bin/python3
""" Python script that Exports data in the JSON format"""

import json
import requests
import sys

if __name__ == "__main__":

    id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    t_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

    x = requests.get(user_url).json()
    todo = requests.get(t_url).json()

    with open('{}.json'.format(id), 'w') as json_file:
        tasks = []
        for y in todo:
            tasks.append({"task": y.get("title"),
                          "completed": y.get("completed"),
                          "username": x.get("username")})

        data = {"{}".format(id): tasks}
        json.dump(data, json_file)
