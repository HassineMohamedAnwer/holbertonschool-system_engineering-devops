#!/usr/bin/python3
""" Exports data """

if __name__ == "__main__":
    import json
    import requests
    import sys

    url_user = requests.get("https://jsonplaceholder.typicode.com/users")
    users = url_user.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    todoAll = {}

    for user in users:
        taskList = []

        for task in todos:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        todoAll[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todoAll, f)
