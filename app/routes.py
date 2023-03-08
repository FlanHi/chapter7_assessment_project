from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, ProForm

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', title='Index')

@app.route('/product', methods=['GET', 'POST'])
def product():
    form=ProForm()
    if form.validate_on_submit():
        flash(f'Product Added Successfully ')
    return render_template('product.html', title='About Me', form=form)

@app.route('/register', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash(f'Register Succesful')
    return render_template('login.html', title='Log in', form=form)