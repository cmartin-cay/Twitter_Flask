from config import api
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    tweets = db.relationship('Tweet', backref='author', lazy='dynamic')
    @staticmethod
    def get_tweets(user):
        """Get most recent tweets (up to the Twitter limit)"""
        user_id = User.query.filter_by(username=user).first()
        try:
            most_recent = user_id.tweets.order_by(Tweet.timestamp.desc()).first().tweetid
        except AttributeError:
            most_recent = 1000000
        all_tweets = []
        # get the first batch of 200 tweets
        new_tweets = api.user_timeline(id=user, since_id=most_recent, count=200)
        all_tweets.extend(new_tweets)
        # get the id of the oldest tweet (then one fewer will be new tweets)
        oldest = all_tweets[-1].id - 1
        # cycle over all remaining tweets that we can access
        while new_tweets:
            new_tweets = api.user_timeline(id=user, count=200, since_id=most_recent, max_id=oldest)
            all_tweets.extend(new_tweets)
            oldest = all_tweets[-1].id - 1

        for tweet in all_tweets:
            post = Tweet(body=tweet.text, timestamp=tweet.created_at, tweetid=tweet.id_str, author=user_id)
            db.session.add(post)
            db.session.commit()

        # ids = [tweet.id for tweet in all_tweets if search in tweet.text]
        # addresses = []
        # for id in ids:
        #     addresses.append('https://twitter.com/{}/status/{}'.format(user, id))
        # return addresses

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(160))
    tweetid = db.Column(db.String(30), index=True, unique=True)
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
