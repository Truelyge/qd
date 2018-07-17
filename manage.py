
from flask_script import Manager
from app import *

manage = Manager(app)

if __name__ == "__main__":
    manage.run()