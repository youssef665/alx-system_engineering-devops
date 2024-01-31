#!/usr/bin/python3


def top_ten(subreddit):
    """Queries the Reddit API and returns"""

    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)

    if sub_info.status_code >= 300:
        print('None')

    else:
        [print(child.get("data").get("title"))
         for child in sub_info.json().get("data").get("children")]
