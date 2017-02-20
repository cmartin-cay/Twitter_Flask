import os
import tweepy

WTF_CSRF_ENABLED = True
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

SECRET_KEY = "You'll never guess"

CONSUMER_KEY = '9MN9cFpVcbZ2wlc57sfg74Axj'
CONSUMER_SECRET = 'iiHgrTshRmdelmamMKngKGjzYkm470y6IwN0f37GzmEXdYqC8J'
ACCESS_TOKEN = '740888554008543232-no2bQMabXhoZLH6OwsRzTipor4hVDbw'
ACCESS_SECRET = 'ENbIKVKx1WNluQI87BMyV0TzcfvEtnm0jHchvVIgHJzCJ'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

