#!/usr/bin/python3
"""My module"""

import json
import requests
import sys

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

    with open("{}.json".format(employee_id), "w") as outfile:
        user_tasks = []
        
        for i in range(len(todo_json_response)):
            task = todo_json_response[i]
            
            user_task = {}
            user_task["task"] = task.get("title")
            user_task["completed"] = task.get("completed")
            user_task["username"] = user_name
          
            user_tasks.append(user_task)
        
        user = { employee_id: user_tasks }
        
        json.dump(user, outfile)
