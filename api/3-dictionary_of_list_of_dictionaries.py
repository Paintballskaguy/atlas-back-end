#!/usr/bin/python3

"""
This script retrieves and displays an employee's TODO list progress
using the JSONPlaceholder API. It accepts an employee ID as a parameter
and outputs the completed tasks and the overall task progress.
"""
import json
import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """
    Retrieves and displays the TODO list progress for a given employee.

    Args:
        employee_id (int): The ID of the employee.
    """
    user_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        )
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found")
        return

    employee_name = user_response.json().get("name")

    todos_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        )
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
            "completed": task{"completed"}
        }
        for task in todos if task["userId"] == user_id
    ]

    data[str(user_id)] = user_tasks

    json_filename = "todo_all_employees.json"
    with open(json_filename, mode="w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script_name.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            fetch_employee_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")
