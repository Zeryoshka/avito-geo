'''
module with handler for GET and stuff for it
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
        return err.messages, 400, HEADERS
    value, message = storage.get(data['KEY'])
    res = {
        'message': message,
        'value': value
    }
    return res, 201, HEADERS