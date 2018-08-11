# Example usage of Twitter API on Google Cloud Functions

## Overview

This sample demonstrates use of the Twitter API in a Google Cloud Function
using the Python 3.7 runtime. It also contains a helper script that you might
find useful for local development.

When you deploy your function, it must contain the following two files:

**Required**

* `main.py` contains your function code
* `requirements.txt` contains your function's dependencies

**Optional**

* `test.py` is a helper script for local development

## Deploying your function

You can use the `gcloud` tool in a shell to deploy your function. Alternatively,
you can paste the code from `main.py` and `requirements.txt` into the Google
Cloud Console.

To deploy using `gcloud`:

```console
$ gcloud beta functions deploy my_twitter_function --trigger-http --entry-point getTweets --runtime python37
```

## Testing your deployed function

Test your function using a tool like `curl`.

First, get your function's URL:

```console
$ YOUR_HTTP_TRIGGER_URL=$(gcloud functions describe my_twitter_function --format='value(httpsTrigger.url)')
```

Then send a POST request to your function using `curl`:

```console
$ curl -d '{"keyword":"google"}' -H "Content-Type: application/json" -X POST $YOUR_HTTP_TRIGGER_URL
```

## Testing your function locally

Set up a virtual environment that uses Python 3 and has the dependencies listed
in `requirements.txt`.

Next, launch the test script:

```console
$ python test.py
 * Serving Flask app "test" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 185-903-498
```

Your function is now running locally using Flask's local development server.

Send a test query to your local function using `curl`:

```console
$ curl -d '{"keyword":"google"}' -H "Content-Type: application/json" -X POST 
http://127.0.0.1:8080
```

## Author

stewart.reichling@gmail.com

