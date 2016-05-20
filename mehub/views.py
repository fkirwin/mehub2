from flask import render_template
from mehub.classes import *
from mehub.customfunctions import *

from . import app
##from .database import session, Entry
from flask import flash
##from flask.ext.login import login_user
from werkzeug.security import check_password_hash
##from .database import User
##from flask.ext.login import login_required
from flask import request, redirect, url_for, session
##from flask.ext.login import current_user
import time
##from flask.ext.login import logout_user
from mehub.customfunctions import getSentiment
from mehub.classes import *


PAGINATE_BY = 10

@app.route("/", methods=["GET"])
def homepage():
    return render_template("homepage.html")
    

@app.route("/analysispage", methods=["GET"])
def analysispage_get():
    return render_template("analysispage.html")

@app.route("/analysispage", methods=["POST"])
def analysispage_post():
    payload=request.form['content']
    anonymize=request.form['anonymize']
    analyze=request.form['analyze']
    reccomendize=request.form['reccomendize']
    
    if anonymize:
        return redirect(url_for('analyzeresultspage'))
    elif analyze:
        session['analyzePost']=payload
        return redirect(url_for('analyzeresultspage'))
    elif reccomendize:
        return redirect(url_for('analyzeresultspage'))
    
@app.route("/analyzeresultspage", methods=["GET"])  
def analyzeresults_get():
    post=getSentiment('analyzePost')
    postPos=.999##post['pos']
    postNeg=post['neg']
    overall=verdictEvaluate(postPos, postNeg)
    return render_template("analyzeresultspage.html", 
    postPos=postPos, 
    postNeg=postNeg,
    overall=overall)


@app.route("/login", methods=["GET"])
def login_get():
    """
    return render_template("login.html")
    """
    
@app.route("/login", methods=["POST"])
def login_post():
    """
    email = request.form["email"]
    password = request.form["password"]
    user = session.query(User).filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash("Incorrect username or password", "danger")
        return redirect(url_for("login_get"))
    else:
        login_user(user)
        return redirect(url_for("entries"))
    """


@app.route('/logout', methods=["GET"])
def logout_get():
    """
    logout_user()
    flash('You were logged out')
    return render_template("login.html")
    """
    
    
    


@app.route("/entry/add", methods=["GET"])
##@login_required
def add_entry_get():
    ##return render_template("add_entry.html")
    pass
    


@app.route("/entry/add", methods=["POST"])
##@login_required
def add_entry_post():
    """"
    entry = Entry(
        title=request.form["title"],
        content=request.form["content"],
        author=current_user
    )
    session.add(entry)
    session.commit()
    time.sleep(5)
    return redirect(url_for("entries"))
    """
    
@app.route("/entry/<id>", methods=["GET"])
def viewentry(id):
    """
    viewentriesid = session.query(Entry.id).filter(Entry.id==id)
    viewentrydetails = session.query(Entry).filter(Entry.id==id)
    return render_template("view_entry.html",
        view_entry=viewentriesid,
        viewentrydetails=viewentrydetails
    )
    """
    
@app.route("/entry/<id>/edit", methods=["GET"])
def editentry_get(id):
    """
    editentryid= session.query(Entry.id).filter(Entry.id==id).all()
    edittitle= session.query(Entry.title).filter(Entry.id==id).all()
    editcontent= session.query(Entry.content).filter(Entry.id==id).all()
    
    return render_template("editentry.html",
    edit_entryid=editentryid[0],
    edit_entrytitle=edittitle[0],
    edit_entrydetails=editcontent[0])
    """

@app.route("/entry/<id>/edit", methods=["POST"])
def editentry_post(id):
    """
    entrytitle=request.form["title"]
    entrycontent=request.form["content"]
    session.query(Entry).filter_by(id=id).update({"title": entrytitle, "content":entrycontent})
    session.commit()
    return redirect(url_for("entries"))
    """
    

@app.route("/entry/<id>/delete", methods=['GET', 'POST'])
def delete_entry(id):
    """
    if request.method=='GET':
        return render_template("delete_entry.html")
    if request.method=='POST':
        if request.form["submitdelete"]=="submitdelete":
            session.query(Entry).filter(Entry.id==id).delete()
            session.commit()
            return redirect(url_for("entries"))
        elif request.form["cancel"]=="cancel":
            return redirect(url_for("entries"))
    """

    