'''
Init module of handlers's package
'''

from typing import Any, Dict, Tuple
from flask import request


from .set import set_handler
from .get import get_handler
from .list_requests import lget_handler, lset_handler
from .ping import ping_handler
