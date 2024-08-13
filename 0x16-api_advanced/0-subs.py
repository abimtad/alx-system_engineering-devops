#!/usr/bin/python3
"""
Module that queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of
    subscribers for a given subreddit. If the subreddit is invalid,
    returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data['data'].get('subscribers', 0)

    except requests.exceptions.RequestException:
        return 0


if __name__ == "__main__":
    print(number_of_subscribers("programming"))
    print(number_of_subscribers("this_is_a_fake_subreddit"))
