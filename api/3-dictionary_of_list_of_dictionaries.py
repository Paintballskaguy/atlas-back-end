#!/usr/bin/python3

"""
This script retrieves and displays an employee's TODO list progress
using the JSONPlaceholder API. It accepts an employee ID as a parameter,
outputs the completed tasks and
the overall task progress, and exports the data to JSON.
"""

import json
import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """
    Retrieves and exports the TODO list progress for a given employee.

    Args:
        employee_id (int): The ID of the employee.
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/"
    user_response = requests.get(user_url)
    users = user_response.json()

    todos_url = (
        f"https://jsonplaceholder.typicode.com/users/todos"
        )
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    data = {
        str(employee_id): [
            {
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            }
            for task in todos
        ]
    }

    json_filename = f"{employee_id}.json"
    with open(json_filename, mode="w") as json_file:
        json.dump(data, json_file)

    print(f"Data exported to {json_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script_name.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            fetch_employee_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")
