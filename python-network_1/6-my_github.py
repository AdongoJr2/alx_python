#!/usr/bin/python3
"""My module"""

import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/users"
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get("{}/{}".format(url, username),
                            headers={"Authorization": password})
    try:
        jsonResponse = response.json()
        try:
            print(jsonResponse["id"])
        except:
            print("None")
    except Exception as e:
        pass
