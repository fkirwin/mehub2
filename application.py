import os
from flask.ext.script import Manager
from mehub import app
from mehub.database import session, Entry, User
from getpass import getpass
from flask.sessions import SessionInterface, SessionMixin
from werkzeug.security import generate_password_hash


manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)



@manager.command
def adduser():
    name = input("Name: ")
    email = input("Email: ")
    password = ""
    password_2=""
    if session.query(User).filter_by(email=email).first():
        print("User with that email address already exists")
        return
    
    while len(password) < 8 or password != password_2:
        password = getpass("Password: ")
        password_2 = getpass("Re-enter password: ")
    user = User(name=name, email=email,
                password=generate_password_hash(password))
    session.add(user)
    session.commit()
if __name__ == "__main__":
    manager.run()
    app.secret_key="fredtestkey"


