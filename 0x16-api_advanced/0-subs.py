#!/usr/bin/python3
"""getsubs

Return: number of subs of a sub
"""
import requests

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    for a given subreddit. If an invalid subreddit is given,
    the function returns 0.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers of the subreddit.
        If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    headers = {'User-Agent': 'MyBot/0.1'}
    
    try:
        
        response = requests.get(url, headers=headers)
    
        if response.status_code == 200:
            data = response.json()
            
            if 'data' in data and 'subscribers' in data['data']:
               
                return data['data']['subscribers']
            else:
             
                return 0
        else:
            return 0
    except requests.RequestException as e:
        print("Error:", e)
        return 0
