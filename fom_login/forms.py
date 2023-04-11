from flask_wtf import FlaskForm
from wtforms import StringField, EmailField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo


class RegistrationForm(FlaskForm):
    name = StringField(label='User Name', validators=[DataRequired(),Length(min=3, max=10)])
    email_id = EmailField(label="Email", validators=[DataRequired(),Email()])
    password = PasswordField(label="Password", validators=[DataRequired(),Length(min=5, max=16)])
    confirm_password = PasswordField(label="Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField(label="Register")


class LoginForm(FlaskForm):
    email_id = EmailField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=5, max=16)])
    submit = SubmitField(label="Login")