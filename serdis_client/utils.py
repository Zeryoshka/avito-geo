'''
Some specific functions for serdis_client
'''
import re

def is_valid_key(key: str):
    '''
    Function for validation keys
    (It needs for minimisation requests to server)
    '''
    return re.fullmatch(r'[a-zA-Z_][a-zA-Z0-9_]*', key) is not None