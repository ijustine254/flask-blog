from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class WikiForm(Form):
    search = StringField('Search here ...',validators=[DataRequired])
    submit = SubmitField('Search')