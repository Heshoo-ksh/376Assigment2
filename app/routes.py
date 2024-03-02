import json
import re
from app import app

@app.route('/tweets')
def get_all_tweets():
    """
    Retrieve and return all tweets.
    
    Returns:
        A JSON object containing a list of tweets with their creation time, ID, and text.
    """
    # Open and read the JSON file containing the tweets archive.
    with open('data/favs.json', 'r') as f:
        favs_data = json.load(f)  # Load the JSON content into a Python dictionary.

    # List comprehension to pick necessary fields from each tweet.
    tweets = [{"created_at": tweet["created_at"], "id": tweet["id"], "text": tweet["text"]} for tweet in favs_data]
    
    return {"tweets": tweets}

@app.route('/tweets/links')
def get_all_links():
    """
    Extract and return all external links found in the tweet texts.
    
    Returns:
        A JSON object where each key is a tweet ID and its value is a list of links found in that tweet's text.
    """
    with open('data/favs.json', 'r') as f:
        favs_data = json.load(f)
    
    links = {}  
    url_pattern = r'https?://[^\s]+'  # Regex pattern to match http and https URLs.
    
    # Extract URLs from each tweet's text.
    for tweet in favs_data:
        # Find all URLs in the tweet's text using the regex pattern.
        tweet_links = re.findall(url_pattern, tweet["text"])
        if tweet_links:
            links[tweet["id"]] = tweet_links
    
    return {"links": links}

@app.route('/tweet/<tweet_id>')
def get_tweet_details(tweet_id):
    """
    Retrieve and return details of a specific tweet by its ID.
    
    Parameters:
        tweet_id (str): The ID of the tweet to retrieve.
    
    Returns:
        A JSON object containing the tweet's creation time, text, and the user's screen name.
        If the tweet is not found, returns an error message.
    """
    with open('data/favs.json', 'r') as f:
        favs_data = json.load(f)
    
    for tweet in favs_data:
        if str(tweet["id"]) == tweet_id:
            return {
                "created_at": tweet["created_at"],
                "text": tweet["text"],
                "user_screen_name": tweet["user"]["screen_name"]
            }
    
    return {"error": "Tweet not found"}, 404

@app.route('/user/<screen_name>')
def get_user_profile(screen_name):
    """
    Retrieve and return detailed profile information of a specific Twitter user by screen name.
    
    Parameters:
        screen_name (str): The screen name of the Twitter user to retrieve.
    
    Returns:
        A JSON object containing the user's location, description, followers count, and friends count.
        If the user is not found, returns an error message.
    """
    with open('data/favs.json', 'r') as f:
        favs_data = json.load(f)
    
    for tweet in favs_data:
        if tweet["user"]["screen_name"].lower() == screen_name.lower():
            user = tweet["user"]
            return {
                "location": user["location"],
                "description": user["description"],
                "followers_count": user["followers_count"],
                "friends_count": user["friends_count"]
            }
    
    return {"error": "User not found"}, 404
