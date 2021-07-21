'''
Init module of handlers's package
'''

from typing import Any, Dict, Tuple
from flask import request

def ping_handler() -> (Tuple[Any, int, Dict[str, str]]):
    '''
    Handler for PING request
    '''
    data = request.get_json()
    if not data:
        data = 'PONG'
    return data, 200, {'Content-Type': 'application/json'}