#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import requests
from sys import argv
if __name__ == "__main__":
    r = requests.post(argv[1], {"email": argv[2]})
    print(r.text)
