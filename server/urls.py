'''
Module with connection handlers to app
'''

from . import app
from .handlers import ping_handler

app.add_url_rule(
    '/ping',
    'ping',
    ping_handler,
    methods=['POST']
)