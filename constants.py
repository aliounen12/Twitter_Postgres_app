import os

CONSUMER_KEY = os.environ.get('consumer_ket')
CONSUMER_SECRET = os.environ.get('consumer_secret')

REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'

