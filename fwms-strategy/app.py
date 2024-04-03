import os
import secrets
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import login_user, current_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = '4f2bfa6592418c6a7e50573998ce99db'

class Login(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Login')

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    return render_template('login.html')

@app.route('/first')
def first():
    return render_template('first.html')

@app.route("/home")
@login_required
def home():
    return redirect(url_for('home'))

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)