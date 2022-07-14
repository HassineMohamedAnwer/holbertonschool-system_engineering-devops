#!/usr/bin/python3
"""queries the Reddit API and returns a list """

import requests


def recurse(subreddit, list=[], count=0, after=None):
    """ytfg"""
    req = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subreddit),
                       params={"count": count, "after": after},
                       headers={"User-Agent": "Aziz"},
                       allow_redirects=False)

    if req.status_code >= 400:
        return None

    ml = list + [child.get("data").get("title")
                 for child in req.json().get("data")
                 .get("children")]

    reqs = req.json()
    if not reqs.get("data").get("after"):
        return ml

    return recurse(subreddit, ml, reqs.get("data").get("count"),
                   reqs.get("data").get("after"))
