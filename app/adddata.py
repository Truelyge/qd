from app.models import *
from app import db


def adddata():
    try:
        user1 = User(name="apple", number=999)
        db.session.add(user1)
        db.session.commit()
        user2 = User(name="eggplant", number=1000)
        db.session.add(user2)
        db.session.commit()
        user3 = User(name="fish", number=1001)
        db.session.add(user3)
        db.session.commit()
        user4 = User(name="rice", number=1002)
        db.session.add(user4)
        db.session.commit()
        user5 = User(name="flower", number=1003)
        db.session.add(user5)
        db.session.commit()
        user6 = User(name="beef", number=1004)
        db.session.add(user6)
        db.session.commit()
        user7 = User(name="banana", number=1006)
        db.session.add(user7)
        db.session.commit()
        user8 = User(name="peach", number=1007)
        db.session.add(user8)
        db.session.commit()
        user9 = User(name="cabbage", number=1008)
        db.session.add(user9)
        db.session.commit()
        user10 = User(name="pork", number=1009)
        db.session.add(user10)
        db.session.commit()
        user11 = User(name="wheat", number=1010)
        db.session.add(user11)
        db.session.commit()
        user12 = User(name="pine", number=1011)
        db.session.add(user12)
        db.session.commit()
        from werkzeug.security import generate_password_hash
        admin1 = Admin(name="admin1", pwd=generate_password_hash("123"))
        db.session.add(admin1)
        db.session.commit()
    except:
        pass
