#!/usr/bin/python3
""" Reddit API. """

import requests


def top_ten(subreddit):
    """ Function query in API of reddit.com and return
    the number of subscribers.
    """
    respn = requests.get(
        'https://www.reddit.com/r/{}/hot.json?limit=10'.format(
            subreddit), allow_redirects=False)
    if respn.status_code == 200:
        respn_data_json = respn.json()
        for key_title in respn_data_json['data']['children']:
            if 'data' in key_title:
                print(key_title['data']['title'])
    else:
        print(None)
