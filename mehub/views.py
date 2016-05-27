from mehub.classes import *
from mehub.customfunctions import *
from flask.sessions import SessionInterface, SessionMixin
from . import app
from mehub.database import session, Entry, User
from werkzeug.security import check_password_hash
from flask import request, redirect, url_for, flash, render_template
import flask
import time
from mehub.customfunctions import getSentiment
from mehub.classes import *
from werkzeug.contrib.cache import SimpleCache
from flask.ext.login import login_required, logout_user, current_user, login_user
from werkzeug.security import generate_password_hash



@app.route("/", methods=["GET"])
def homepage():
    return render_template("homepage.html")
    

@app.route("/analysispage", methods=["GET"])
@login_required
def analysispage_get():
    return render_template("analysispage.html")

@app.route("/analysispage", methods=["POST"])
@login_required
def analysispage_post():
    payload=request.form["content"]
    ##thisPost=analyzePost(post=payload)
    ##session['payload']=payload
    cache.set('payload', payload, timeout=500)
    anonymize=request.form["anonymize"]
    analyze=request.form["analyze"]
    reccomendize=request.form["reccomendize"]
    
    if anonymize:
        return redirect(url_for('analyzeresultspage'))
    elif analyze:
        return redirect(url_for('analyzeresultspage', payload=payload))
    elif reccomendize:
        return redirect(url_for('analyzeresultspage'))
        
    
@app.route("/analyzeresultspage", methods=["GET", "POST"])
@login_required
def analyzeresults_get():
    payload=cache.get('payload')
    ##stuff=session['payload']
    ##payload = request.args['payload']  # counterpart for url_for()
    ###payload = session['payload']       # counterpart for session
    post=getSentiment(payload)
    postPos=post['pos']
    postNeg=post['neg']
    overall=verdictEvaluate(postPos, postNeg)
    evalpost=post
    return render_template("analyzeresultspage.html", 
    postPos=postPos, 
    postNeg=postNeg,
    overall=evalpost)

@app.route("/createaccount", methods=["GET", "POST"])  
def createAccount():
    if request.method=='GET':
            return render_template("createaccount.html")
    elif request.method=='POST':
        email = request.form["email"]
        password = request.form["password"]
        passwordconfirm=request.form["passwordConfirm"]
        if password==passwordconfirm:
            user = User(
                email = email,
                password = generate_password_hash(password))
            session.add(user)
            session.commit()
            time.sleep(3)
            flash('You successfully created an account.')
            login_user(user)
            return redirect(url_for("homepage"))
    
"""
@app.route("/login", methods=["GET", "POST"])  
def login():
    if request.method=='GET':
        return render_template("login.html")
    elif request.method=='POST':
        email = request.form["email"]
        password = request.form["password"]
        user = session.query(User).filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash("Incorrect username or password", "danger")
            return redirect(url_for("login"))
        else:
            login_user(user)
            return redirect(url_for("homepage"))
"""

@app.route("/login", methods=["GET"])
def login_get():
    return render_template("login.html")
    
@app.route("/login", methods=["POST"])
def login_post():
    email = request.form["email"]
    password = request.form["password"]
    user = session.query(User).filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash("Incorrect username or password", "danger")
        return redirect(url_for("login"))
    else:
        login_user(user)
        return redirect(url_for("homepage"))
"""
@app.route('/logout', methods=["GET"])
def logout_get():
    logout_user()
    flash('You were logged out')
    return render_template("login.html")
    """