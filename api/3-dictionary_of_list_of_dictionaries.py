#!/usr/bin/python3
"""My module"""

import json
import requests

if __name__ == "__main__":
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    todo_response = requests.get(todo_url)
    todo_json_response = todo_response.json()

    with open("todo_all_employees.json", "w") as outfile:
        user_tasks = []

        for i in range(len(todo_json_response)):
            task = todo_json_response[i]

            user_id = task.get("userId")

            user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
                user_id)
            user_response = requests.get(user_url)
            user_json_response = user_response.json()

            user_name = user_json_response.get("name")

            user_task = {}
            user_task["username"] = user_name
            user_task["task"] = task.get("title")
            user_task["completed"] = task.get("completed")
            
            print(user_task)

            user_tasks.append(user_task)

        user = {user_id: user_tasks}

        json.dump(user, outfile)
