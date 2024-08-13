#!/usr/bin/python3
"""
Module that queries the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit. If no results are
found for the given subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, return None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}
    params = {'limit': 100, 'after': after}
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        posts = data['data'].get('children', [])
        if not posts:
            return None if not hot_list else hot_list
        hot_list.extend(post['data']['title'] for post in posts)
        after = data['data'].get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    except requests.exceptions.RequestException:
        return None


if __name__ == "__main__":
    result = recurse("programming")
    if result is not None:
        print(len(result))
    else:
        print("None")
    result = recurse("this_is_a_fake_subreddit")
    if result is not None:
        print(len(result))
    else:
        print("None")
