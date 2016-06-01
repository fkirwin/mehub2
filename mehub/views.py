from mehub.classes import *
from mehub.customfunctions import *
from flask.sessions import SessionInterface, SessionMixin
from . import app
from mehub.database import session, Entry, User
from werkzeug.security import check_password_hash
from flask import request, redirect, url_for, flash, render_template
import flask
import time
from mehub.customfunctions import getSentiment, sentenceStructure, randomizePost, sentenizer
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

@app.route("/analysispage", methods=["GET","POST"])
def analysispage_post():
    if request.method=="GET":
        render_template('analysispage.html')
    elif request.method=='POST':
        entry = Entry(
            content=request.form["content"],
            author=current_user
            )
        session.add(entry)
        session.commit()
        time.sleep(5)
        if 'anonymize'in request.form.values():
            return redirect(url_for('analyzeresultspage'))
        elif 'analyze' in request.form.values():
            return redirect(url_for('analyzeresults_get'))
        elif 'reccomendize' in request.form.values():
            return redirect(url_for('analyzeresultspage'))
        
    
@app.route("/analyzeresultspage", methods=["GET", "POST"])
def analyzeresults_get():
    if request.method=="GET":
        payload=session.query(Entry.content).filter(Entry.author_id==flask.session['user_id']).order_by(Entry.id.desc()).first()
        post=getSentiment(payload[0])
        postPos=post['pos']
        postNeg=post['neg']
        overall=verdictEvaluate(postPos, postNeg)
        words=sentenceStructure(payload[0])
        neighbors = mrRogers(payload[0])
        return render_template("analyzeresultspage.html", 
        postPos=postPos, 
        postNeg=postNeg,
        overall=overall,
        words = words
        ##word = word,
        ##neighbor=neighbor
        )

@app.route("/anonymize", methods=["GET"])
def anonymize_get():
    payload=session.query(Entry.content).filter(Entry.author_id==flask.session['user_id']).order_by(Entry.id.desc()).first()
    yodaSays=yodaizePost(payload[0])
    randomize= randomizePost(payload[0])
    return render_template("anonymizeresultspage.html",
    yodaSays = yodaSays,
    randomize = randomize
        )


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