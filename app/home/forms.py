# _*_ coding: utf-8 _*_


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField, FloatField, \
    SelectMultipleField,RadioField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from app.models import Sign_in


class Sign_inForm(FlaskForm):

    number = StringField(
        label="工号",
        description="",
        render_kw={
            "class": "form-control",
            "id": "input_title",
            "placeholder": "请输入员工工号",  # 占位符
        }
    )

    type = RadioField(
        'Type',
        choices=[('0', '上班签到'), ('1', '下班签到')],
        validators=[DataRequired()]
    )

    submit = SubmitField(
        "签到",
        render_kw={
            "class": "btn btn-primary btn-block btn-flat",
        }
    )
