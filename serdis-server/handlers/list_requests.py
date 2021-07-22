'''
module with handler for LSET and stuff for it
'''
from typing import Any, Dict, Tuple
from flask import request
from marshmallow import ValidationError

from . import schemas
from .. import storage
from .headers import HEADERS


def lset_handler() -> (Tuple[Any, int, Dict[str, str]]):
    '''
    Handler for command LSET which set or update list by key
    '''
    json_data = request.get_json()
    try:
        data = schemas.LSET.load(json_data)
    except ValidationError as err:
        res = {
            'is_created': False,
            'message': err.messages
        }
        return res, 400, HEADERS

    if 'TTL' in data:
        ttl = data['TTL']
    else:
        ttl = None
    
    created, message = storage.lset(data['KEY'], data['VALUE'], ttl)
    res = {
        'is_created': created,
        'message': message
    }
    return res, 201, HEADERS


def lget_handler() -> (Tuple[Any, int, Dict[str, str]]):
    '''
    Handler for command LGET which get list by key
    '''
    json_data = request.get_json()
    try:
        data = schemas.LGET.load(json_data)
    except ValidationError as err:
        res = {
            'is_created': False,
            'message': err.messages
        }
        return res, 400, HEADERS
    
    value, message = storage.lget(data['KEY'])
    res = {
        'message': message,
        'value': value
    }
    return res, 201, HEADERS
