import os
import unittest
from config import basedir
from app import app, db
from app.models import User, Tweet
from datetime import datetime

# class TestCse(unittest.TestCase):
    # def setUp(self):
    #     app.config['TESTING'] = True
    #     app.config['WTF_CSRF_ENABLED'] = False
    #     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
    #     self.app = app.test_client()
    #     db.create_all()
    #
    # def tearDown(self):
    #     db.session.remove()
    #     db.drop_all()
    #
    # def test_user(self):
    #     u1 = User(username='User1')
    #     db.session.add(u1)
    #     db.session.commit()
    #     assert User.username == 'User1'

# u1 = User(username='Alice')
# db.session.add(u1)
# db.session.commit()
# user = User.query.filter_by(username='NotGbo').first()
#print(user.username)
# print(user.tweets.order_by(Tweet.timestamp.desc()).first().tweetid)
# posts = user.tweets.order_by(Tweet.timestamp.desc()).first()
# print(posts.tweetid)
# search = Tweet.query.filter_by(author=user).filter(Tweet.body.contains("vanilla")).all()
# for each in search:
#     print(each.body, each.tweetid)