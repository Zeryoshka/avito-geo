'''
Module with handlers for all data-structures
'''

from . import schemas
from .headers import HEADERS, TEXT_HEADERS
from .. import storage

from typing import Any, Dict, Tuple
from flask import request
from marshmallow import ValidationError


def keys_handler() -> (Tuple[Any, int, Dict[str, str]]):
    '''
    Handlers for KEY query - query for getting keys-list
    '''
    res = {
        'keys': storage.keys()
    }
    return res, 200, HEADERS

def del_handler() -> (Tuple[Any, int, Dict[str, str]]):
    '''
    Handler for DEL query - query for deleting key from storage
    '''
    json_data = request.get_json()
    try:
        data = schemas.DEL.load(json_data)
    except ValidationError as err:
        res = {
            'is_deleted': False,
            'message': err.messages
        }
        return res, 400, HEADERS
    
    deleted, message = storage.delete(data['KEY'])
    res = {
        'is_deleted': deleted,
        'message': message
    }
    if deleted:
        return res, 200, HEADERS
    return res, 400, HEADERS

def ping_handler() -> (Tuple[Any, int, Dict[str, str]]):
    '''
    Handler for PING request (checking server connection)
    '''
    return 'PONG', 200, TEXT_HEADERS