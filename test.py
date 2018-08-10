from flask import Flask, request
from main import getTweets


app = Flask(__name__)


@app.route('/', methods=['POST'])
def invoke_user_function():
    return getTweets(request)


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)