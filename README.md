Flask Twitter Favorites API

Overview
This Flask application provides a RESTful API to interact with a stored JSON archive of Twitter favorites. It allows users to retrieve all tweets, extract links from tweets, get details of specific tweets, and user profiles.

Prerequisites
- Python 3 (with `pip` included)
- Flask
  
Setup Instructions

Step 1: Install Python
Ensure you have Python installed on your system. If you do not, you can download and install it from python.org.

Step 2: Clone the Repository
Clone the project repository to your local machine. If you use Git, you can run the following command:
git clone https://github.com/Heshoo-ksh/376Assigment2.git

Step 3: Install Flask
Navigate to the project directory:
cd path/to/project

Install Flask using pip. This command needs to be run only once.
Run command: pip install Flask

Step 4: Running the Application
To run the application, use the following command:
python app.py
This command starts a local development server. By default, the server runs on http://127.0.0.1:5000/, and you can access the API endpoints from there.

API Endpoints
- `/tweets` - Retrieves all tweets.
- `/tweets/links` - Retrieves all external links found in tweets.
- `/tweet/<tweet_id>` - Retrieves details of a specific tweet by its ID.
- `/user/<screen_name>` - Retrieves detailed profile information of a specific Twitter user by screen name.

Dependencies
This project requires the following Python packages:
- Flask: A lightweight WSGI web application framework. (This is the only external dependency required for this project.)
- JSON: Included in Python's standard library, used for parsing and generating JSON data. 
- re: Python's standard regex library, used for extracting links from tweet texts.


