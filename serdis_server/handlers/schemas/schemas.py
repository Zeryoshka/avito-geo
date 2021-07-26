'''
Module with description marshmallow.Schema classes
'''

from marshmallow import Schema
from marshmallow.fields import Int, String, List
from marshmallow.validate import Length, Range, NoneOf

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


class LsetSchema(Schema):
    '''
    LSET-request schema
    '''
    KEY = KeyValidator(required=True)
    VALUE = List(String(), required=True, validate=Length(min=1))
    TTL = Int(validate=Range(min=1))


class LgetSchema(Schema):
    '''
    LSET-request schema
    '''
    KEY = KeyValidator(required=True)

class DelSchema(Schema):
    '''
    DEL-request schema
    '''
    KEY = KeyValidator(required=True)