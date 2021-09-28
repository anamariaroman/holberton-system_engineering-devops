#!/usr/bin/python3
""" Reddit API. """

import requests


def recurse(subreddit, hot_list=[], after=""):
    """ Function query in API of reddit.com and return
    the number of subscribers.
    """
    URL = 'https://www.reddit.com/r/{}/hot.json?limit={}&after={}'.format(
        subreddit, LIMIT, after)
    r = requests.get(URL, headers=HEADERS, allow_redirects=False)
    if r.status_code >= 400:
        return None
    response_json = r.json()
    if response_json['data']['children'][0]['kind'] == 't3':
        for post in response_json['data']['children']:
            hot_list.append(post['data']['title'])
    after = response_json['data']['after']
    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
