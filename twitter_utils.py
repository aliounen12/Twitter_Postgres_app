import constants
import oauth2
import urllib.parse as urlparse

# Create a consumer, which uses CONSUMER_KEY AND CONSUMER_SECRET to identify our app uniquely
consumer = oauth2.Consumer(constants.CONSUMER_KEY, constants.CONSUMER_SECRET)


def get_request_token():
    # Make a client with the consumer credentials so that you can perform a request
    client = oauth2.Client(consumer)

    # Use the Client to perform a request to get a request token from twitter
    response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')
    if response.status != 200:
        print('An error occurred getting the request token from twitter')

    # Get the request token and parse the query string that is returned
    # Query string has the token and a secret token
    return dict(urlparse.parse_qsl(content.decode('utf-8')))

def get_oauth_verifier(request_token):
    # We ask the user to authorize our app by going to the following site - authorization url
    # from twitter and a query string attached which is the oauth request token
    print('Go to the following site in your browser:')
    print(get_oauth_verifier_url(request_token))

    # Ask the user for the pin that twitter gives to them
    return input('What is the Pin? ')

def get_oauth_verifier_url(request_token):
    return '{}?oauth_token={}'.format(constants.AUTHORIZATION_URL, request_token['oauth_token'])

def get_access_token(request_token, oauth_verifier):
    # Create an oauth token instance with the request token and the secret request token
    token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])

    # Set the verifier of that token which is the pin
    token.set_verifier(oauth_verifier)

    # Create a new client that has both the consumer app credentials and the user credentials stored in the token instance
    client = oauth2.Client(consumer, token)

    # Make a request to the access token url from twitter with the client
    response, content = client.request(constants.ACCESS_TOKEN_URL, 'POST')

    # parse the response just like before and store the access token details in a dictionary
    return dict(urlparse.parse_qsl(content.decode('utf-8')))
