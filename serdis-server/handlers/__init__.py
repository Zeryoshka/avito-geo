'''
Init module of handlers's package
'''

from typing import Any, Dict, Tuple
from flask import request


from .set import set_handler
from .get import get_handler
from .lset import lset_handler
# from .lget improt lget_handler
from .ping import ping_handler
