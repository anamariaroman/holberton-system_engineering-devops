#!/usr/bin/python3
""" Reddit API. """


import requests


def number_of_subscribers(subreddit):
    """ Function query in API of reddit.com and return
    the number of subscribers.
    """
    respn = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(
            subreddit), allow_redirects=False)
    if respn.status_code == 200:
        respn_data_json = respn.json()
        return respn_data_json['data']['subscribers']
    return(0)
