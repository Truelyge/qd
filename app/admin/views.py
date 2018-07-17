# _*_ coding: utf-8 _*_

import codecs
import os
import uuid
from datetime import datetime
from app import db, app
from functools import wraps
from . import admin
from flask import render_template, redirect, url_for, flash, session, request, g, abort
from app.admin.forms import LoginForm, UserForm, E_UserForm
from app.models import Admin, User, Sign_in
from werkzeug.utils import secure_filename


@admin.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(name=data["name"]).first()
        if admin:
            if not admin.check_pwd(data["pwd"]):
                flash("密码错误！", "err")
                return redirect(url_for("admin.login"))
        else:
            flash("账户不存在！", "err")
            return redirect(url_for("admin.login"))
        session["admin"] = admin.name
        session["admin_id"] = admin.id
        return redirect(url_for("admin.index"))
    return render_template("admin/login.html", form=form)


@admin.route("/logout/")
def logout():
    session.pop("admin", None)
    session.pop("admin_id", None)
    return redirect(url_for("home.index"))


@admin.route("/index/")
def index():
    return render_template("admin/admin.html")


@admin.route("/user_add/", methods=["GET", "POST"])
def user_add():
    form = UserForm()
    if form.validate_on_submit():
        data = form.data
        user = User(
            name=data["name"],
            number=data["number"]
        )
        db.session.add(user)
        db.session.commit()
        flash("添加员工成功！", "ok")
        return redirect(url_for("admin.user_add"))
    return render_template("admin/user_add.html", form=form)


@admin.route("/user_list/<int:page>/", methods=["GET"])
def user_list(page=None):
    if page is None:
        page = 1
    users = User.query.all()
    page_data = User.query
    page_data = page_data.paginate(page=page, per_page=6)
    return render_template("/admin/user_list.html", page_data=page_data)


@admin.route("/user_edit/<int:id>/", methods=["GET", "POST"])
def user_edit(id=None):
    form = E_UserForm()
    user2 = User.query.get_or_404(int(id))
    if request.method == "GET":
        form.name.data = user2.name
        form.number.data = user2.number
        # form.workings=user.workings
    if form.validate_on_submit():
        data = form.data
        user_count = User.query.filter_by(number=data["number"]).count()
        try:
            if user_count == 1 and user2.name != data["name"]:
                flash("员工号已经存在！", "err")
                return redirect(url_for("admin.user_edit",id=id))
        except:
            pass
        user2.name = data["name"]
        user2.number = data["number"]
        db.session.add(user2)
        db.session.commit()
        flash("修改员工信息成功！", "ok")
        return redirect(url_for("admin.user_edit",id=id))
    return render_template("admin/user_edit.html", form=form, user2=user2)


@admin.route("/sign_in_list/<int:page>/<int:id>/", methods=["GET"])
def sign_in_list(id=None, page=None):
    user = User.query.filter_by(id=id).first()
    if page is None:
        page = 1
    #page_data = Sign_in.query
    #page_data = page_data.filter_by(user_id=id)
    #page_data = page_data.paginate(page=page, per_page=6)
    page_data=Sign_in.query.filter(
        Sign_in.user_id==user.id
    ).order_by(
        Sign_in.s_time.desc()
    ).paginate(page=page,per_page=6)
    # print(page_data)
    # print(type(page_data))
    return render_template("admin/sign_in_list.html", page_data=page_data,user=user)


@admin.route("/user_del/<int:id>", methods=["GET"])
def user_del(id=None):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash("员工删除成功！", "ok")
    return redirect(url_for("admin.user_list", page=1))
