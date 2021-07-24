'''
Module with handlers for all data-structures
'''

from . import schemas
from .headers import HEADERS
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
    return res, 400, HEADERS