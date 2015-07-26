from wtforms import Form
from wtforms import fields
from wtforms import validators


class MessageForm(Form):
    message_id = fields.IntegerField(
        "Message ID",
        validators=[
            validators.required(),
            validators.NumberRange(min=0),
        ],
    )
    order = fields.IntegerField(
        "Order",
        validators=[
            validators.required(),
            validators.NumberRange(min=1, max=6),
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
        ],
    )
