import json
import re
from app import app

@app.route('/')
def hello():
    return "Hello, World!"


@app.route('/load-favs')
def load_favs():
    with open('data/favs.json', 'r') as f:  # Adjust path as necessary
        favs_data = json.load(f)
    return favs_data

# Get all tweets (create time, id, and tweet text) available in the archive.
@app.route('/tweets')
def get_all_tweets():
    with open('data/favs.json', 'r') as f:
        favs_data = json.load(f)
    tweets = [{"created_at": tweet["created_at"], "id": tweet["id"], "text": tweet["text"]} for tweet in favs_data]
    return {"tweets": tweets}

#Get a list of all external links (all links that appear in tweet text field. 
#Use regular expressions to extract the links, the links should be grouped based on tweet ids.
@app.route('/tweets/links')
def get_all_links():
    with open('data/favs.json', 'r') as f:
        favs_data = json.load(f)
    links = {}
    url_pattern = r'https?://[^\s]+'
    for tweet in favs_data:
        tweet_links = re.findall(url_pattern, tweet["text"])
        if tweet_links:
            links[tweet["id"]] = tweet_links
    return {"links": links}

#Get the details (tweet created_at, text, user screen_name) about a given tweet (given the tweet’s id).
@app.route('/tweet/<tweet_id>')
def get_tweet_details(tweet_id):
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

#Get detailed profile (location, description, followers_count, friends_count) information about a given Twitter user (given the user’s screen name).
@app.route('/user/<screen_name>')
def get_user_profile(screen_name):
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
