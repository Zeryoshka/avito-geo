'''
Module with connection handlers to app
'''

from . import app
from .handlers import ping_handler, \
    set_handler, get_handler, lset_handler, lget_handler, \
    keys_handler

app.add_url_rule(
    '/ping',
    'PING',
    ping_handler,
    methods=['GET']
)

app.add_url_rule(
    '/set',
    'SET',
    set_handler,
    methods=['POST']
)

app.add_url_rule(
    '/get',
    'GET',
    get_handler,
    methods=['POST']
)

app.add_url_rule(
    '/lset',
    'LSET',
    lset_handler,
    methods=['POST']
)

app.add_url_rule(
    '/lget',
    'LGET',
    lget_handler,
    methods=['POST']
)

app.add_url_rule(
    '/keys',
    'KEYS',
    keys_handler,
    methods=['GET']
)