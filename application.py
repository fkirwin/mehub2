import os
from flask.ext.script import Manager
from mehub import app
from mehub.database import session, Entry, User, Base
from getpass import getpass
from flask.sessions import SessionInterface, SessionMixin, SecureCookieSession
from werkzeug.security import generate_password_hash


manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

@manager.command
def adduser():
    email = "creator@mehub.com"
    password = "password"
    password_2="password"
    user = User(email=email,
                password=generate_password_hash(password))
    session.add(user)
    session.commit()
    
    
if __name__ == "__main__":
    manager.run()
    app.secret_key="fredtestkey"


