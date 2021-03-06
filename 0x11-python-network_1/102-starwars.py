#!/usr/bin/python3
"""takes in a string and sends a search request to the Star Wars API"""
from requests import get
from sys import argv
if __name__ == "__main__":
    page = 1
    json = get("https://swapi.co/api/people/?search={}&page={}".
               format(argv[1], page)).json()
    print("Number of results: {}".format(json.get("count")))
    try:
        while json.get("count"):
            for arg in json.get("results"):
                print(arg.get("name"))
                for film in arg.get("films"):
                    print("\t{}".format(get(film).json().get("title")))
            page += 1
            json = get("https://swapi.co/api/people/?search={}&page={}".
                       format(argv[1], page)).json()
    except Exception:
        pass
