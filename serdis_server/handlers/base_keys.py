'''
module with handler for base Value data-structure and stuff for it
'''

from typing import Any, Dict, Tuple
from flask import request
from marshmallow.exceptions import ValidationError

from .headers import HEADERS
from . import schemas
from .. import storage

def get_handler() -> (Tuple[Any, int, Dict[str, str]]):
    '''
    handler for GET request (get key-value pair)
    '''
    json_data = request.get_json()
    
    try:
        data = schemas.GET.load(json_data)
    except ValidationError as err:
        res = {
            'value': None,
            'message': err.messages
        }
        return res, 400, HEADERS
    value, message = storage.get(data['KEY'])
    res = {
        'message': message,
        'value': value
    }
    return res, 201, HEADERS

def set_handler() -> (Tuple[Any, int, Dict[str, str]]):
    '''
    handler for SET request (set key-value pair)
    '''
    json_data = request.get_json()
    try:
        data = schemas.SET.load(json_data)
    except ValidationError as err:
        res = {
            'value': None,
            'message': err.messages
        }
        return res, 400, HEADERS

    if 'TTL' in data:
        ttl = data['TTL']
    else:
        ttl = None
    
    created, message = storage.set(data['KEY'], data['VALUE'], ttl)
    res = {
        'is_created': created,
        'message': message
    }
    if created:
        return res, 201, HEADERS
    return res, 400, HEADERS