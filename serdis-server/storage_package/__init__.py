'''
Init module of storage package
'''

from typing import Tuple
from .data_structures import Value, ValueList


class Storage():
    '''
    Storage class holding all information
    '''

    def __init__(self):
        '''
        Create new storage object
        '''
        self.values = dict()

    def _is_key_exist_for_other_type(self, key: str, type_: type) -> (bool):
        '''
        Return True if key already exist for other data structure
        '''
        return (
            key in self.values and 
            not isinstance(self.values[key], type_)
        )


    def _get_validator(self, key: str, type_: type):
        '''
        Validator get-requests(GET, LGET, HGET)
        '''
        if key not in self.values:
            return None, 'Key is not exist'
        value = self.values[key]
        if not value.is_alive:
            del self.values[key]
            return None, 'Key is not exist'
        if not isinstance(value, type_):
            return None, 'Value mismatch'
        return value.value, 'Ok'

    def set(self, key: str, value: str, ttl: int = None):
        '''
        set Value by key, make pair key-value in storage,
        can set TTL if ttl not is None

        if key uses for other type of datastructure returns errors message

        Returns: tuple with
            is_created: bool
            message: str
        '''
        if self._is_key_exist_for_other_type(key, Value):
            return False, f'key "{key}" already uses for other datastructure'
        
        self.values[key] = Value(value, ttl)
        return True, 'Ok'

    def get(self, key: str) -> (Tuple[str, str]):
        '''
        Get Value by key if it's exist and alive
        If key is not exist, is not alive or has mismatch in type returns None

        Returns: 
            value - str
            message - str
        '''
        return self._get_validator(key, Value)
    
    def lset(self, key: str, value: str, ttl: int = None):
        '''
        set List by key, make pair key-value in storage,
        can set TTL if ttl not is None

        if key uses for other type of datastructure returns errors message

        Returns: tuple with
            is_created: bool
            message: str
        '''
        if self._is_key_exist_for_other_type(key, ValueList):
            return False, f'key "{key}" already uses for other datastructure'
        
        self.values[key] = ValueList(value, ttl)
        return True, 'Ok'

    def lget(self, key: str):
        '''
        set List by key, make pair key-value in storage,
        can set TTL if ttl not is None

        if key uses for other type of datastructure returns errors message

        Returns: tuple with
            is_created: bool
            message: str
        '''
        return self._get_validator(key, ValueList)
