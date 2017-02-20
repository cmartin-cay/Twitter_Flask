from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class UserField(FlaskForm):
    nickname = StringField('nickname', validators=[DataRequired()])
    search = StringField('search')
    # search = StringField('search', validators=[DataRequired()])