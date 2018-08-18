"""A function that shows use of the Twitter API client."""
import flask
import twitter


# Note: these should probably not be stored in plaintext
consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token_key = 'ACCESS_TOKEN_KEY'
access_token_secret = 'ACCESS_TOKEN_SECRET'

# Initialize an API client outside of the function scope to minimize latency
# on successive invocations. This code should only execute on a "cold start"
api = twitter.Api(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token_key=access_token_key,
    access_token_secret=access_token_secret)


def entrypoint(request):
    """ Resonds to an HTTP POST request containing a keyword used to query
    the Twitter API. Outputs tweets matching the keyword.

    Args:
        request (flask.Request): The request object containing POST data
    Returns:
        tweets (str): JSON-ified representation of tweets matching the query
    """

    # Check the request method. This function only accepts POST but this can
    # be changed to suit your needs
    if request.method != 'POST':
        return 'Error: invalid method, function expects POST'

    # Get JSON from the Flask request object
    data = request.get_json()

    # The request object's POST body must contain `keyword`
    if 'keyword' in data:
        # Create a query based on the value associated with `keyword`
        keyword = data['keyword']
        query = (f'q={keyword}'
                 ' -Athletics, -Sports, -Basketball, -Football&count=100')
        result = api.GetSearch(raw_query=query) 

        # Convert results to a list of (tweet id, tweet text)
        output = [(tweet.id, tweet.text) for tweet in result]

        # JSON=ify the list of tweets and return to the client
        return flask.jsonify(output)
    else:
        return 'Error: POST body does not contain `keyword`'
