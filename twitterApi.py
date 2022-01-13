import tweepy, imagemanipulator

consumer_key = 'xxxx'
consumer_secret = 'xxxx'
access_token = 'xxxx'
access_token_secret = 'xxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

image = open('processedImages/done3.png', 'rb')
file = 'processedImages/done3.png'
imagemanipulator.manipultor()


media = api.media_upload(filename = file)
tweet = imagemanipulator.rand
post_result = api.update_status(status = tweet, media_ids =[media.media_id])


