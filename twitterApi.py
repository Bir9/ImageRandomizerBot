import tweepy, imagemanipulator

consumer_key = 'DPt4NGxTE3rYghjJDtaqsu2P8'
consumer_secret = 'uZEKoCiijELnA6qqQgyqrIHkgQLaDfSqh5YYexm1CmfGeB7aZZ'
access_token = '1478900221019099136-ej9hIUpMnQyg9OZHaP8uyvTMorjuHX'
access_token_secret = 'worOPDHO6xrSH2w6O34BvQt9uVwhjnYQvq2xm7oB9ird7'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

image = open('processedImages/done3.png', 'rb')
file = 'processedImages/done3.png'
imagemanipulator.manipultor()


media = api.media_upload(filename = file)
tweet = imagemanipulator.rand
post_result = api.update_status(status = tweet, media_ids =[media.media_id])


