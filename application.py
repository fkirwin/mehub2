import os
from flask.ext.script import Manager

from mehub import app
##from mehub.database import session, Entry
from getpass import getpass

##from werkzeug.security import generate_password_hash

##from mehub.database import User

manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
    


if __name__ == "__main__":
    manager.run()