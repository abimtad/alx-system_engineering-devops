#!/usr/bin/python3
"""This script uses a REST API to get information about a given employee ID
and returns information about his/her TODO list progress."""
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url)
    user = response.json()
    name = user.get("name")

    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    response = requests.get(url)
    todos = response.json()
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          len(completed_tasks),
                                                          total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
