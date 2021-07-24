'''
Init module of handlers's package
'''

from typing import Any, Dict, Tuple
from flask import request


from .base_keys import set_handler, get_handler
from .list_requests import lget_handler, lset_handler
from .ping import ping_handler
from .others_handlers import keys_handler
