from flask import render_template, redirect, url_for, flash
from app import app, db
from config import api
import tweepy
from .forms import UserField, SearchField
from .models import User, Tweet


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UserField()
    if form.validate_on_submit():
        user = form.username.data
        u = User.query.filter_by(username=user).first()
        current_id = api.user_timeline(id=user, count=1)[0].id_str
        # If it's a new user, add them to the database
        if u is None:
            u1 = User(username=user)
            db.session.add(u1)
            db.session.commit()
        # If the user exists, check if the most recent tweet in db and real life are the same
        elif u.tweets.order_by(Tweet.timestamp.desc()).first().tweetid == current_id:
            flash("No new tweets since last reviewed")
            return redirect(url_for('user', username=user))
        User.get_tweets(user)
        flash('Database has been updated')
        return redirect(url_for('user', username=user))
    return render_template('index.html',
                           title="Home",
                           form=form)


@app.route('/<username>', methods=['GET', 'POST'])
def user(username):
    addrs=""
    form = SearchField()
    if form.validate_on_submit():
        username = username
        search = form.search.data
        u = User.query.filter_by(username=username).first()
        search = Tweet.query.filter_by(author=u).filter(Tweet.body.contains(search)).all()
        addrs = [('https://twitter.com/{}/status/{}'.format(tweet.author.username, tweet.tweetid)) for tweet in search]
    return render_template('user.html',
                           title='User',
                           username=username,
                           form=form,
                           addrs=addrs)
