# _*_ coding: utf-8 _*_

from datetime import datetime
from functools import wraps

import os
from werkzeug.utils import secure_filename

import uuid
from werkzeug.security import generate_password_hash
from app import db, app
from app.home.forms import Sign_inForm
from app.models import Sign_in, User, Day, Month, Year
from . import home
from flask import render_template, url_for, redirect, flash, session, request, Response
import flask
import time


@home.route("/", methods=["GET", "POST"])
def index():
    """
    签到
    """
    form = Sign_inForm()
    # hobby = flask.request.form.getlist('hobby')
    # print(hobby)
    if form.validate_on_submit():
        try:
            data = form.data
            # print(data["gender"])
            now1 = datetime.now()
            user = User.query.filter_by(number=data["number"]).first()
            # print(user)
            sign_in = Sign_in(
                user_id=user.id,
                s_type=data["type"],
                s_time=now1
            )
            db.session.add(sign_in)
            db.session.commit()
            # print(data["type"],type(data["type"]))
            if data["type"] == str(1):
                """
                print("hello")
                sign_in1 = Sign_in.query.filter_by(s_time=now1).first()
                print(sign_in1)
                sign_in2 = Sign_in.query.filter_by(id=(sign_in1.id - 1)).first()
                print(sign_in2.s_type,type(sign_in2.s_type))
                if sign_in2.s_type == 0:
                    print("jhhh")
                    working = sign_in2.s_time - sign_in1.s_time
                    print(working)
                    # user = User.query.filter_by(number=data["number"])
                    workings = user.workings
                    print(workings)
                    workings = workings + working
                    print(workings)
                    user.workings = workings
                    db.session.add(user)
                    db.session.commit()
                """
                # print("ok")
                sign = Sign_in.query.filter_by(user_id=user.id).all()
                # print(type(sign))
                le = len(sign)
                sign_in1 = sign[le - 1]
                # print(sign_in1)
                sign_in2 = sign[le - 2]
                # print(sign_in2)
                if sign_in2.s_type == 0:
                    print("jhhh")
                    working = sign_in1.s_time - sign_in2.s_time
                    print(sign_in2.s_time, sign_in1.s_time)
                    print(working)
                    work = working.days + working.seconds / 3600
                    print(work)
                    # user = User.query.filter_by(number=data["number"])
                    workings = user.workings
                    print(workings)
                    workings = workings + work
                    print(workings)
                    user.workings = workings
                    db.session.add(user)
                    db.session.commit()
            else:
                sign = Sign_in.query.filter_by(user_id=user.id).all()
                le = len(sign)
                sign_in1 = sign[le - 1]
                sign_in2 = sign[le - 2]
                if sign_in2.s_type == 0 and le>1:
                    flash("已经进行了上班签到！", "err")
                    return redirect(url_for("home.index"))
            flash("签到成功！", "ok")
        except:
            print("err")
            db.session.rollback()
    return render_template("home/sign_in.html", form=form)


@home.route("/check/")
def check():
    users = User.query.all()
    now = datetime.now()
    for user in users:
        today = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
        day = Day(
            day=today,
            workhours=user.workings,
            user_id=user.id
        )
        db.session.add(day)
        db.session.commit()
        user.workings = 0.0
        db.session.add(user)
        db.session.commit()
        if now.day == 1:
            month = str(now.year) + "-" + str(now.month - 1)
            dayshours = 0.0
            days = Day.query.filter_by(user_id=user.id).all()
            for da in days:
                if da.day > month:
                    dayshours = dayshours + da.workhours
            month = Month(
                month=month,
                workhours=dayshours,
                user_id=user.id
            )
            db.session.add(month)
            db.session.commit()
            if now.month == 1:
                year = str(now.year - 1)
                monthshours = 0.0
                months = Month.query.filter_by(user_id=user.id).all()
                for mon in months:
                    if mon.month > year:
                        monthshours = monthshours + mon.workhours
                year = Year(
                    year=year,
                    workhours=monthshours,
                    user_id=user.id
                )
                db.session.add(year)
                db.session.commit()
    return redirect(url_for("home.index"))
