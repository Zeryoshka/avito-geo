'''
Module with description marshmallow.Schema classes
'''

from marshmallow import Schema
from marshmallow.fields import Int, String
from marshmallow.validate import Range, NoneOf

from .key_validator import KeyValidator


class SetSchema(Schema):
    '''
    SET-request schema
    '''
    KEY = KeyValidator(required=True)
    VALUE = String(required=True, validate=NoneOf(['']))
    TTL = Int(validate=Range(min=1))


class GetSchema(Schema):
    '''
    GET-request schema
    '''
    KEY = KeyValidator(required=True)