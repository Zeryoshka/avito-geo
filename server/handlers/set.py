'''
module with handler for SET and stuff for it
'''

from typing import Any, Dict, Tuple
from marshmallow.exceptions import ValidationError
from flask import request

from .headers import HEADERS
from . import schemas
from .. import storage

def set_handler() -> (Tuple[Any, int, Dict[str, str]]):
    '''
    handler for SET request (set key-value pair)
    '''
    json_data = request.get_json()
    try:
        data = schemas.SET.load(json_data)
    except ValidationError as err:
        return err.messages, 400, HEADERS

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