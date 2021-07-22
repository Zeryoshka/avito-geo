'''
module with handler for PING and stuff for it
'''

from typing import Any, Dict, Tuple
from flask import request

from .headers import TEXT_HEADERS

def ping_handler() -> (Tuple[Any, int, Dict[str, str]]):
    '''
    Handler for PING request (checking server connection)
    '''
    return 'PONG', 200, TEXT_HEADERS