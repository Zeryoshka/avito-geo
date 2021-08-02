'''
Some specific functions for serdis_client
'''
import re
from typing import List
from pyparsing import Suppress, Word, ZeroOrMore, alphas, Optional

def is_valid_key(key: str):
    '''
    Function for validation keys
    (It needs for minimisation requests to server)
    '''
    return re.fullmatch(r'[a-zA-Z_][a-zA-Z0-9_]*', key) is not None


template = Suppress('[') + Suppress('"') + ZeroOrMore(Word(alphas+'_+')+Suppress('"')+Suppress(',')) + Optional(Word(alphas)) + Suppress(']')
def list_parse(line: str) -> (List[str]):
    '''
    Function for parse list from console to python list
    '''
    