#!/usr/bin/python3
"""My module"""

import csv
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

    # open the file in the write mode
    f = open("{}.csv".format(employee_id), "w")

    # create the csv writer
    writer = csv.writer(f, lineterminator="\n")

    for i in range(len(todo_json_response)):
        task = todo_json_response[i]

        task_values = [
            "{}".format(employee_id),
            "{}".format(user_name),
            "{}".format(task.get("completed")),
            "{}".format(task.get("title")),
        ]

        # write a row to the csv file
        writer.writerow(task_values)

    # close the file
    f.close()
