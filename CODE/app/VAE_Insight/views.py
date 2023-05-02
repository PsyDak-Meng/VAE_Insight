import os
from flask import render_template, render_template_string, request, url_for, redirect, flash, session
from flask_login import login_user, login_required, logout_user, current_user
from markupsafe import escape
from VAE_Insight import app, db
from VAE_Insight.models import User
from VAE_Insight.forms import LoginForm, RegistrationForm, EditInfoForm
from VAE_Insight.model.model import *
from VAE_Insight.model.input_output_config import input_to_numeric


def get_features(user):
    features = [
        {"key":'feature1', "value": user.feature1},
        {"key":'feature2', "value": user.feature2},
        {"key":'feature3', "value": user.feature3},
        {"key":'feature4', "value": user.feature4},
        {"key":'feature5', "value": user.feature5},
        {"key":'feature6', "value": user.feature6},
        {"key":'feature7', "value": user.feature7},
        {"key":'feature8', "value": user.feature8},
        {"key":'feature9', "value": user.feature9},
        {"key":'feature10', "value": user.feature10},
        {"key":'feature11', "value": user.feature11},
        {"key":'feature12', "value": user.feature12},
        {"key":'feature13', "value": user.feature13},
        {"key":'feature14', "value": user.feature14},
        {"key":'feature15', "value": user.feature15},
        {"key":'feature16', "value": user.feature16},
        {"key":'feature17', "value": user.feature17},
        {"key":'feature18', "value": user.feature18},
        {"key":'feature19', "value": user.feature19},
        {"key":'feature20', "value": user.feature20},
        {"key":'feature21', "value": user.feature21}
    ]
    return features

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if "Prediction" in request.form.values():
        return redirect(url_for('prediction_result'))
    form = EditInfoForm()
    user = get_current_user()
    if user is None: features = []
    else: features = get_features(user)
    return render_template("prediction.html", features=features, form=form)

@app.route('/prediction_result', methods=['GET', 'POST'])
def prediction_result():
    user = get_current_user()
    features = get_features(user)
    features_list = []
    for feature in features:
        features_list.append(feature['value'])
    features_list = input_to_numeric(features_list)
    prediction_result_list = renderPredictionResult(features_list)
    # print(prediction_result_list)
    return render_template("prediction_result.html", result=prediction_result_list)

@app.route('/instruction', methods=['GET', 'POST'])
def instruction():
    return render_template("instruction.html")

@app.route('/referenced', methods=['GET', 'POST'])
def referenced():
    return render_template("referenced.html")

@app.route('/introduction', methods=['GET', 'POST'])
def introduction():
    return render_template("introduction.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash('LOGIN SUCCESS.')
            session['username'] = user.username
            return redirect(url_for('index'))
        else:
            flash('INVALID EMAIL OR PASSWARD.')
            return render_template('login.html', form=form)
    else:
        print(form.errors)
        return render_template('login.html', form=form)

@app.route('/factors', methods=['GET', 'POST'])
def factors():
    return redirect(url_for('/dashapp/'))

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        print(form.errors)
        return render_template('registration.html', form=form)

@app.route('/edit_info', methods=['GET', 'POST'])
def edit_info():
    form = EditInfoForm()
    if form.validate_on_submit():
        user = get_current_user()
        user.feature1 = form.feature1.data
        user.feature2 = form.feature2.data
        user.feature3 = form.feature3.data
        user.feature4 = form.feature4.data
        user.feature5 = form.feature5.data
        user.feature6 = form.feature6.data
        user.feature7 = form.feature7.data
        user.feature8 = form.feature8.data
        user.feature9 = form.feature9.data
        user.feature10 = form.feature10.data
        user.feature11 = form.feature11.data
        user.feature12 = form.feature12.data
        user.feature13 = form.feature13.data
        user.feature14 = form.feature14.data
        user.feature15 = form.feature15.data
        user.feature16 = form.feature16.data
        user.feature17 = form.feature17.data
        user.feature18 = form.feature18.data
        user.feature19 = form.feature19.data
        user.feature20 = form.feature20.data
        user.feature21 = form.feature21.data
        db.session.commit()
        features = get_features(user)
        return redirect(url_for('prediction', features=features))
    else:
        print(form.errors)
        return render_template('edit_info.html', form=form)


def get_current_user():
    username= session.get('username', None)
    if username is not None:
        user = User.query.filter_by(username=username).first()
        return user
    return None
