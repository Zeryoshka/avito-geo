'''
module with handler for PING and stuff for it
'''

from typing import Any, Dict, Tuple
from flask import request

from .headers import HEADERS

def ping_handler() -> (Tuple[Any, int, Dict[str, str]]):
    '''
    Handler for PING request (checking server connection)
    '''
    data = request.get_json()
    if not data:
        data = 'PONG'
    return data, 200, HEADERS