# twitter-summarizer-rest-service-dabadi9

## API Desicription

This API will return a .txt file with all the tweets from the past 2 days from a specified account. If the tweet contains any type of media, it will transform the media into words using Google Vision. Each tweet is displayed in a separate line.

## Setup

You need to have python 3 and install the requirements, so run:

```bash
pip install -r requirements.txt.
```

You need to put your twitter keys in a file named "keys" and your google vision keys in a file named "key.json". Both files should be on the main project directory.

## Start server

```bash
python application.py
```

## Get demo video

Make a get request to "http://127.0.0.1:5000/getvideo/". The API will return a video containing demo.

## Get text file from a specific handle

Make a get request to "http://127.0.0.1:500/gettext/<% HANDLE %>" where <% HANDLE %> is the Twitter handle for any user.

## AWS

The application is runnning in an AWS Elastic Beanstalk with base URL "http://ec500c1v2-env.eba-t8aqpadz.us-east-2.elasticbeanstalk.com/".