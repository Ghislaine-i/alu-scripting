#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Return total subscribers for a given subreddit."""
    # Set custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyRedditApp/1.0'}

    # Reddit API endpoint for subreddit info
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Send GET request, but don't follow redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if subreddit exists and request was successful
    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    else:
        # Invalid subreddit or redirect
        return 0
