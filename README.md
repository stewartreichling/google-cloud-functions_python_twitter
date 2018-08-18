# Using the Twitter API client with Google Cloud Functions

## Overview

This sample demonstrates use of the Twitter API client with Google Cloud
Functions on the Python 3.7 runtime.

## Set up your local development environment

### Pre-requisites
* The Python 3.7 interpreter
* `pip`
* `virtualenv`
* `curl`
* Developer credentials for the Twitter API
* The `gcloud` command-line tool

### Create and activate a virtual environment
Use `virtualenv` to create a python3 virtual environment:
```console
$ virtualenv --python python3 env
```

Activate your newly-created virtual environment:
```console
$ source env/bin/activate
```

### Install dependencies
Use `pip` to install project dependencies:
```console
pip install -r requirements.txt
```

## Run locally
Execute the `bin/test-local` script to run your function locally using Flask's
local development server:
```console
$ bash bin/test-local
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

Now open another shell and use `curl` to send a query to your local function:
```console
$ curl -d '{"keyword":"cats"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8080
```

## Deploy your function
Execute the `bin/test-local` script to deploy a function named `twitter_client`
using `gcloud`:

```console
$ bash bin/deploy
Deploying function (may take a while - up to 2 minutes)...done.
```

Alternatively, you can paste the code from `main.py` and `requirements.txt`
into the Google Cloud Console.

## Test your deployed function
Execute the `bin/test-deployed` script to send an HTTP request to your deployed
function:

```console
$ bash bin/test-deployed
```