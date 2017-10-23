"""Simple example using flask wtform and validators."""
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddressForm(Form):
    """Address form with a simple validator."""

    address = StringField('Address', validators=[DataRequired("address?")])
    submit = SubmitField("Search")
