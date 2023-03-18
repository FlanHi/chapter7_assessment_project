from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    """Login Form"""
    username = StringField('Username', validators=[DataRequired(), Length(1, 16)])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Login')

class ProForm(FlaskForm):
    """Product Form"""
    pro_name = StringField('Product Name', validators=[DataRequired(), Length(1, 16)])
    pro_desc = StringField('Product description', validators=[DataRequired()])
    stock = SelectField(u'In Stock', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    submit = SubmitField('Add product')