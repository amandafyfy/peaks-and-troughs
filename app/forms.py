from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Please use a different username.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Please use a different email address.")


class AttemptForm(FlaskForm):
    question_1_ans = SelectField(
        u"Question 1",
        choices=[("cpp", "C++"), ("py", "Python"), ("text", "Plain Text")],
        validators=[DataRequired()],
    )
    question_2_ans = SelectField(
        u"Question 2",
        choices=[("cpp", "C++"), ("py", "Python"), ("text", "Plain Text")],
        validators=[DataRequired()],
    )
    question_3_ans = SelectField(
        u"Question 3",
        choices=[("cpp", "C++"), ("py", "Python"), ("text", "Plain Text")],
        validators=[DataRequired()],
    )
    question_4_ans = SelectField(
        u"Question 4",
        choices=[("cpp", "C++"), ("py", "Python"), ("text", "Plain Text")],
        validators=[DataRequired()],
    )
    question_5_ans = SelectField(
        u"Question 5",
        choices=[("cpp", "C++"), ("py", "Python"), ("text", "Plain Text")],
        validators=[DataRequired()],
    )
    submit = SubmitField("Submit Attempt")
