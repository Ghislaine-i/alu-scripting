#!/usr/bin/python3
"""
0-subs.py

Query the Reddit API and return the total number of subscribers for a
given subreddit.

Prototype:
    def number_of_subscribers(subreddit)

Behavior:
- Returns the integer number of subscribers for a valid subreddit.
- Returns 0 if the subreddit is invalid, inaccessible, or if an error occurs.
- Does not follow redirects (invalid subreddits may redirect to search results).
- Uses a custom User-Agent to avoid rate limiting.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers for the given subreddit.

    Args:
        subreddit (str): Name of the subreddit (e.g., "python").

    Returns:
        int: Number of subscribers, or 0 if the subreddit is invalid or
             the request fails.
    """
    if not isinstance(subreddit, str) or subreddit.strip() == "":
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyRedditApp/1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
    except Exception:
        pass

    return 0
