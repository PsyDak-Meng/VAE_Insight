from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

class RegistrationForm(FlaskForm):
    username = StringField('username', validators =[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    cpassword = PasswordField('Confirm Password', validators = [DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class EditInfoForm(FlaskForm):
    feature1 = StringField('feature1', validators=[DataRequired()])
    feature2 = StringField('feature2', validators=[DataRequired()])
    feature3 = StringField('feature3', validators=[DataRequired()])
    feature4 = StringField('feature4', validators=[DataRequired()])
    feature5 = StringField('feature5', validators=[DataRequired()])
    feature6 = StringField('feature6', validators=[DataRequired()])
    feature7 = StringField('feature1', validators=[DataRequired()])
    feature8 = StringField('feature2', validators=[DataRequired()])
    feature9 = StringField('feature3', validators=[DataRequired()])
    feature10 = StringField('feature4', validators=[DataRequired()])
    feature11 = StringField('feature5', validators=[DataRequired()])
    feature12 = StringField('feature6', validators=[DataRequired()])
    feature13 = StringField('feature1', validators=[DataRequired()])
    feature14 = StringField('feature2', validators=[DataRequired()])
    feature15 = StringField('feature3', validators=[DataRequired()])
    feature16 = StringField('feature4', validators=[DataRequired()])
    feature17 = StringField('feature5', validators=[DataRequired()])
    feature18 = StringField('feature6', validators=[DataRequired()])
    feature19 = StringField('feature1', validators=[DataRequired()])
    feature20 = StringField('feature2', validators=[DataRequired()])
    feature21 = StringField('feature3', validators=[DataRequired()])

