#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit. If the subreddit is invalid,
    prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}
    params = {'limit': 10}
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        posts = data['data'].get('children', [])
        if not posts:
            print(None)
            return
        for post in posts:
            print(post['data']['title'])
    except requests.exceptions.RequestException:
        print(None)


if __name__ == "__main__":
    top_ten("programming")
    top_ten("this_is_a_fake_subreddit")
