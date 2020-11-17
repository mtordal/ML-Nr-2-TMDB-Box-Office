from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SelectField, RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):

    budget = IntegerField('Budget', validators=[NumberRange(min=0, max=500000000)])
    genres = StringField('Genre', validators=[DataRequired()])
    release_year = IntegerField('Release Year', validators=[NumberRange(min=1850, max=2020)])
    cast = StringField('Cast', validators=[DataRequired()])

    submit = SubmitField('Submit')