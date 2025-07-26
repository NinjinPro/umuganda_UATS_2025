# server/forms/user_forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, RadioField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional, ValidationError

class UserSignupForm(FlaskForm):
    role = RadioField(
        'Role',
        choices=[('citizen', 'Citizen'), ('admin', 'Admin')],
        validators=[DataRequired(message="Please select a role.")]
    )

    is_local = BooleanField('Are you a Rwandan?', validators=[DataRequired()])
    is_not_local = StringField('If not, specify your Country', validators=[Optional()])

    first_name = StringField('First Name', validators=[DataRequired(), Length(max=30)])
    middle_name = StringField('Middle Name', validators=[Optional(), Length(max=60)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=30)])
    gender = SelectField(
        'Gender',
        choices=[
            ('', 'Select Gender'),
            ('male', 'Male'),
            ('female', 'Female'),
            ('transgender', 'Transgender')
        ],
        validators=[Optional()]
    )

    province = StringField('Province', validators=[DataRequired()])
    district = StringField('District', validators=[DataRequired()])
    sector = StringField('Sector', validators=[DataRequired()])
    cell = StringField('Cell', validators=[DataRequired()])
    village = StringField('Village', validators=[DataRequired()])
    isibo = StringField('Isibo', validators=[DataRequired()])

    email = EmailField('Email', validators=[Optional(), Email()])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=9, max=10)])

    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=4),
            EqualTo('confirm', message='Passwords must be a match')
        ]
    )

    confirm = PasswordField('Confirm Password')

    submit = SubmitField('Sign Up')

    # validating is_not_local
    def validate_is_not_local(self, field):
        if not self.is_local.data and not field.data.strip():
            raise ValidationError("If you are not Rwandan, specify your country.")


class UserLoginForm(FlaskForm):
    identifier = StringField(
        'Email or Phone',
        validators=[DataRequired(message="Please enter your email or phone number.")]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=6, message="Password must be at least 6 characters long.")]
    )
    submit = SubmitField('Login')
