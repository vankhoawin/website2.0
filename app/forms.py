from wtforms import Form, StringField, TextAreaField, validators
from wtforms.validators import Email, InputRequired, ValidationError


class ContactForm(Form):
    name    = StringField('Name', validators=[InputRequired()])
    email   = StringField('Name', validators=[InputRequired(), Email()])
    subject = StringField('Name', validators=[InputRequired()])
    message = TextAreaField('Name', validators=[InputRequired()])