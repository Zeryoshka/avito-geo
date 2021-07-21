'''
module with handler for SET and stuff for it
'''

from typing import Any, Dict, Tuple
from marshmallow.exceptions import ValidationError
from flask import request

from .headers import HEADERS
from . import schemas

def set_handler() -> (Tuple[Any, int, Dict[str, str]]):
    '''
    handler for SET request (set key-value pair)
    '''
    json_data = request.get_json()
    
    try:
        data = schemas.SET.load(json_data)
    except ValidationError as err:
        return err.messages, 400, HEADERS
    print(data)
    return 'OK', 201, HEADERS