#!/usr/bin/python3

"""
This script retrieves and displays an employee's TODO list progress
using the JSONPlaceholder API. It accepts an employee ID as a parameter
and outputs the completed tasks and the overall task progress.
"""

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

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    print(
        f"Employee {employee_name} is done with tasks("
        f"{number_of_done_tasks}/{total_tasks}):"
        )

    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script_name.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            fetch_employee_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")
