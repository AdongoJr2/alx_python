#!/usr/bin/python3
"""My module"""

import sys
import requests

if __name__ == "__main__":
    employee_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    user_response = requests.get(user_url)
    user_json_response = user_response.json()

    user_name = user_json_response.get("name")

    todo_url = "{}/todos".format(user_url)
    todo_response = requests.get(todo_url)
    todo_json_response = todo_response.json()

    total_tasks = len(todo_json_response)
    tasks_done = []

    for i in range(total_tasks):
        task = todo_json_response[i]
        is_task_completed = task.get("completed")

        if is_task_completed:
            tasks_done.append(task)

    header = "Employee {} is done with tasks({}/{}):".format(
        user_name, len(tasks_done), total_tasks)

    print("{}".format(header))

    for i in range(len(tasks_done)):
        print("\t {}".format(tasks_done[i].get("title")))
