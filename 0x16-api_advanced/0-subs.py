#!/usr/bin/python3
"""aliiikl,jnjhb"""

import requests
from sys import argv


def number_of_subscribers(subreddit):
    user = {"User-Agent": "Anwer"}
    request = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(subreddit), headers=user)

    if request.status_code == 200:
        return request.json().get("data").get("subscribers")
    else:
        return 0
