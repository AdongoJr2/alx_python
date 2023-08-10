#!/usr/bin/python3
"""My module"""

import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = ""

    try:
        q = sys.argv[1]
    except IndexError:
        pass

    response = requests.post(url, {"q": q})

    try:
        jsonResponse = response.json()
        if len(jsonResponse) == 0:
            print("No result")
        else:
            print("[{}] {}".format(jsonResponse["id"], jsonResponse["name"]))
    except:
        print("Not a valid JSON")
