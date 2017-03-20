#!/usr/bin/env python

# run tweet_download.py file_fith_ids
# output is printed

# fill these in:
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

class TweetDownloader(object):
    def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        self.api = tweepy.API(auth)

    def download(self, tweetIds):
        for status in self.api.statuses_lookup(tweetIds):
                print(status.id, "\t", status.text.replace("\n", " "))
        


if(__name__ == "__main__"):
    import tweepy, sys, time
    from tweepy import OAuthHandler
    downloader = TweetDownloader(consumer_key,\
            consumer_secret, access_token, access_secret)
    chunk = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            if (len(chunk) < 95):
                chunk.append(line.rstrip())
            else:
                chunk.append(line.rstrip())
                downloader.download(chunk)
                chunk = []
                time.sleep(3)
        if (len(chunk) > 0): downloader.download(chunk)






