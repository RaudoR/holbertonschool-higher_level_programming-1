#!/usr/bin/python3
"""takes in a string and sends a search request to the Star Wars API"""
from requests import get
from sys import argv
if __name__ == "__main__":
    json = get("https://swapi.co/api/people/?search={}".
               format(argv[1])).json()
    print("Number of results: {}".format(json["count"]))
    for args in json["results"]:
        print(args["name"])
