#!/usr/bin/python3
"""takes your Github credentials (username and password) and
uses the Github API to display your id
"""
from requests import get
from sys import argv
if __name__ == "__main__":
    json = get("https://api.github.com/repos/{}/{}/commits".
               format(argv[2], argv[1])).json()
    count = 0
    for arg in json:
        count += 1
        name = arg.get("commit").get("author").get("name")
        sha = arg.get("sha")
        print("{}: {}".format(sha, name))
        if count == 10:
            break
