from wtforms import Form
from wtforms import fields
from wtforms import validators

from utils import NumericValidator


class MessageForm(Form):
    id = fields.IntegerField(
        "Scheduled message ID",
        validators=[
            validators.required(),
            NumericValidator.numeric(),
        ],
    )
    message_id = fields.IntegerField(
        "Message ID",
        validators=[
            validators.required(),
            validators.NumberRange(min=0),
            NumericValidator.numeric(),
        ],
    )
    order = fields.IntegerField(
        "Order",
        validators=[
            validators.required(),
            validators.NumberRange(min=1, max=6),
            NumericValidator.numeric(),
        ],
    )
    type_message = fields.SelectField(
        "Type Message",
        choices=[
            ("R", "Recordatorio"),
            ("M", "Motivacional"),
        ],
        validators=[
            validators.required(),
        ],
    )
    message = fields.StringField(
        "Text Message",
        validators=[
            validators.required(),
            validators.Length(max=500),
        ],
    )
    cellphone = fields.IntegerField(
        "Cellphone",
        validators=[
            validators.required(),
            NumericValidator.fixed_digits(digits=9),
        ],
    )


class CallForm(Form):
    id = fields.IntegerField(
        "Scheduled message ID",
        validators=[
            validators.required(),
            NumericValidator.numeric(),
        ],
    )
    message_id = fields.IntegerField(
        "Message ID",
        validators=[
            validators.required(),
            validators.NumberRange(min=0),
            NumericValidator.numeric(),
        ],
    )
    cellphone = fields.IntegerField(
        "Cellphone",
        validators=[
            validators.required(),
            NumericValidator.fixed_digits(digits=9),
        ],
    )


class SMSForm(Form):
    id = fields.IntegerField(
        "Scheduled message ID",
        validators=[
            validators.required(),
            NumericValidator.numeric(),
        ],
    )
    message = fields.StringField(
        "Text Message",
        validators=[
            validators.required(),
            validators.Length(max=500),
        ],
    )
    cellphone = fields.IntegerField(
        "Cellphone",
        validators=[
            validators.required(),
            NumericValidator.fixed_digits(digits=9),
        ],
    )
