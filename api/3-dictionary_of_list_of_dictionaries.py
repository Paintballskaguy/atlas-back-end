#!/usr/bin/python3

"""
This script retrieves and exports the TODO list progress for all employees
using the JSONPlaceholder API.
It exports data to a JSON file in the specified format.
"""

import json
import requests


def fetch_all_employees_todo_progress():
    """
    Retrieves and exports the TODO list progress for all employees
    to a JSON file in the format:
    { "USER_ID": [{"username": "USERNAME",
    "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ] }
    """

    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    users = users_response.json()

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    data = {}
    for user in users:
        user_id = user["id"]
        username = user["username"]

        user_tasks = [
            {
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            }
            for task in todos if task["userId"] == user_id
        ]

        data[str(user_id)] = user_tasks

    json_filename = "todo_all_employees.json"
    with open(json_filename, mode="w") as json_file:
        json.dump(data, json_file)

    print(f"Data exported to {json_filename}")


if __name__ == "__main__":
    fetch_all_employees_todo_progress()
