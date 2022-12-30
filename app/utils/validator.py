from marshmallow import Schema, fields, validate, ValidationError
import re


def validate_password(password):
    if not re.match('(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$<>~$%^&*()_+])', password):
        raise ValidationError(
            "password should at least have an uppercase,lowercase,number and a special character")


def validate_length(input):
    if input.strip() == '':
        raise ValidationError('fields cannot be blank')
    elif not re.match(r"^(?=.*[a-z])[a-zA-Z0-9_.-]{3,25}$", input):
        raise ValidationError("{} is not a valid input".format(input))


def validate_email(email):
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        raise ValidationError("please enter a valid email address")


class UserSchema(Schema):
    username = fields.String(required=True, )
    email = fields.Email(required=True)
    password = password = fields.String(required=True, validate=validate_password)
    user_id = fields.String()
    date_created = fields.String()
    is_admin = fields.String()



class LoginSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)

class WaveSchema(Schema):
    title= fields.String(required=True)
    description = fields.String(required=True)
    user = fields.String()
    category =fields.String()
    date_created = fields.String()
    wave_id = fields.String()

