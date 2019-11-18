from user import User
from database import Database
from twitter_utils import get_request_token, get_oauth_verifier, get_access_token

# Initialize database connection
Database.initialise(dbname='Learning', user='postgres', password='starbar1', host='localhost', port='5433')

screen_name = input('Enter your twitter screen name: ')


user = User.load_from_db_by_screen_name(screen_name)

if not user:
    request_token = get_request_token()

    oauth_verifier = get_oauth_verifier(request_token)

    access_token = get_access_token(request_token, oauth_verifier)

    # Collect other user info
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")

    # Create a user object and save the user info to the database
    user = User(screen_name, access_token['oauth_token'], access_token['oauth_token_secret'])
    user.save_to_db()

tweets = user.twitter_request('https://www.api.twitter.com/1.1/search/tweets.json?q=politics')

for tweet in tweets['statuses']:
    print(tweet['text'])
