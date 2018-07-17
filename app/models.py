# _*_ coding: utf-8 _*_

from datetime import datetime
from app import db


# 用户数据模型
class User(db.Model):
    __tablename__ = "user"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名字
    number = db.Column(db.String(100), unique=True)  # 用户工号
    workings = db.Column(db.Float,default=0.0)  # 工作时长
    sign_in = db.relationship('Sign_in', backref='user')  # 签到表

    def __repr__(self):
        return '<User %r>' % self.name


# 签到表
class Sign_in(db.Model):
    __tablename__ = "sign_in"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # 编号
    s_type = db.Column(db.Integer)  # 签到类型
    s_time = db.Column(db.DateTime, index=True, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属员工

    def __repr__(self):
        return "<Sign_in %r>" % self.id


# 管理员信息模型Admin
class Admin(db.Model):
    __tablename__ = "admin"
    __table_args__ = {"useexisting": True}
    # 数据模型
    id = db.Column(db.Integer, primary_key=True)  # 管理员编号
    name = db.Column(db.String(100), unique=True)  # 管理员名字
    pwd = db.Column(db.String(100))  # 管理员登录密码

    # addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 管理员注册时间

    def __repr__(self):
        return "<Admin %r>" % self.name

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)
