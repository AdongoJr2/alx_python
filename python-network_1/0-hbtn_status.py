#!/usr/bin/python3
"""My module"""

from requests import get

if __name__ == "__main__":
    response = get("https://alu-intranet.hbtn.io/status")
    content = str(response.content, "UTF-8")

    formatted_response = """
Body response:
\t- type: {}
\t- content: {}
""".strip().format(type(content), content)

    print(formatted_response)

    # print("- type: {}".format(type(content)))
    # print("- content: {}".format(content))
