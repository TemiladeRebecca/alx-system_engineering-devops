#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress
"""

import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/"
    employee_url = url + employee_id
    todo_url = url + "todo"

    employee_response = requests.get(employee_url).json()
    todo_response = requests.get(todo_url).json()
    employee_name = employee_response.get("name")
    total = len(todo_response)
    done = 0
    for i in todo_response:
        if i.get("completed"):
            done += 1
    print("Employee {} is done with tasks({}/{}):".
          format(employee_name, done, total))

    for todo in todo_response:
        if todo.get("completed"):
            title = todo.get("title")
            print("\t {}".format(title))
