# _*_ coding: utf-8 _*_


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField, FloatField, \
    SelectMultipleField
from wtforms import validators
from wtforms.validators import DataRequired, ValidationError, EqualTo
from app.models import Admin, User


class LoginForm(FlaskForm):
    name = StringField(
        label="账号",
        validators=[DataRequired("账号不能为空")],  # 验证器
        description="账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！",  # 占位符
        }
    )

    pwd = PasswordField(
        label="密码",
        validators=[DataRequired("密码不能为空")],  # 验证器
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码！",  # 占位符
        }
    )

    submit = SubmitField(
        "登录",
        render_kw={
            "class": "btn btn-primary btn-block btn-flat",
        }
    )

    # 验证账号是否存在
    def validate_account(self, field):
        name = field.data
        admin = Admin.query.filter_by(name=name).count()
        if admin == 0:
            raise ValidationError("账号不存在！")


class UserForm(FlaskForm):
    name = StringField(
        label="名字",
        validators=[DataRequired("名字不能为空")],  # 验证器
        description="名字",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入名字！",  # 占位符
        }
    )

    number = StringField(
        label="工号",
        validators=[DataRequired("工号不能为空")],  # 验证器
        description="工号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入工号！",  # 占位符
        }
    )

    submit = SubmitField(
        "添加",
        render_kw={
            "class": "btn btn-primary",
        }
    )


class E_UserForm(FlaskForm):
    name = StringField(
        label="名字",
        validators=[DataRequired("名字不能为空")],  # 验证器
        description="名字",
        render_kw={
            "class": "form-control",
            "id":"input_name",
            "placeholder": "请输入名字！",  # 占位符
        }
    )

    number = StringField(
        label="工号",
        validators=[DataRequired("工号不能为空")],  # 验证器
        description="工号",
        render_kw={
            "class": "form-control",
            "id": "input_number",
            "placeholder": "请输入工号！",  # 占位符
        }
    )

    submit = SubmitField(
        "修改",
        render_kw={
            "class": "btn btn-primary",
        }
    )
