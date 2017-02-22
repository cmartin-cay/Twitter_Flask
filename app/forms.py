from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class UserField(FlaskForm):
    username = StringField('username', validators=[DataRequired()])

class SearchField(FlaskForm):
    search = StringField('search', validators=[DataRequired()])
