from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,EmailField,FileField,ValidationError
from wtforms.validators import DataRequired,Length,EqualTo
import imghdr

def validate_image(form,field):
    if field.data:
        image_type=imghdr.what(field.data)
        if image_type not in ['jpg', 'jpeg', 'png']:
            raise ValidationError('Invalid image type.')

class RegistrationForm(FlaskForm):
    username=StringField(
        'Username:',
        validators=[DataRequired(),Length(min=5,max=20)]
    )
    email=EmailField(
        'Email:',
        validators=[DataRequired()]
    )
    password=PasswordField(
        'Password:',
        validators=[DataRequired(),Length(min=8)]
    )
    confirm_password=PasswordField(
        'Confirm Password:',
        validators=[DataRequired(),Length(min=8),EqualTo(fieldname='password')]
    )
    submit=SubmitField('Login')

class LoginForm(FlaskForm):
    email=EmailField('Email',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=8)])
    submit=SubmitField('Sign Up')