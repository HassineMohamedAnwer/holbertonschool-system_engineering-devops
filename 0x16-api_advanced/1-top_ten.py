#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 hot posts"""

import json
import requests


def top_ten(subreddit):
    user = {"User-Agent": "Aziz"}
    request = requests.get("https://www.reddit.com/r/{}/hot/.json"
                           .format(subreddit), headers=user)

    if request.status_code == 200:
        count = 0

        for posts in request.json().get("data").get("children"):
            if count < 10:
                print(posts.get("data").get("title"))
                count += 1
    else:
        print(None)
