#!/usr/bin/python3
"""
Module that queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive).
"""

import requests
from collections import defaultdict


def count_words(subreddit, word_list, word_count={}, after=None):
    """
    Recursive function that queries the Reddit API, parses the title of all
    hot articles, and prints a sorted count of given keywords
    (case-insensitive).
    """
    word_list = [word.lower() for word in word_list]

    if not word_count:
        word_count = defaultdict(int)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        posts = data['data'].get('children', [])
        if not posts:
            if not word_count:
                return

            sorted_word_count = sorted(
                word_count.items(), key=lambda kv: (-kv[1], kv[0])
            )
            for word, count in sorted_word_count:
                if count > 0:
                    print(f"{word}: {count}")
            return

        for post in posts:
            title = post['data']['title'].lower().split()
            for word in word_list:
                word_count[word] += title.count(word)

        after = data['data'].get('after')
        if after:
            return count_words(subreddit, word_list, word_count, after)
        else:
            sorted_word_count = sorted(
                word_count.items(), key=lambda kv: (-kv[1], kv[0])
            )
            for word, count in sorted_word_count:
                if count > 0:
                    print(f"{word}: {count}")

    except requests.exceptions.RequestException:
        return


if __name__ == "__main__":
    count_words(
        "programming", [
            "react", "python", "java", "javascript", "scala", "no_results_for_this_one"  # noqa: #E501
        ]
    )
    count_words("programming", ["JavA", "java"])
    count_words("not_a_valid_subreddit", [
        "python", "java", "javascript", "scala", "no_results_for_this_one"
    ])
