'''
Client for python serdis database
'''
from typing import List, Tuple
import requests
from .utils import is_valid_key


class Serdis():
    '''
    Object, for connection and working with serdis
    '''

    def __init__(self, host: str = '127.0.0.1', port: int = 5000):
        '''
        Consructor of Serdis class
        '''
        self._address = f'http://{host}:{port}/'
    
    def ping(self) -> (str):
        '''
        Method for PING query
        '''
        value = requests.get(self._address+'ping').text
        return value

    def get(self, key: str) -> (Tuple[str, str]):
        '''
        Method for getting values by key (GET)

        Returns: Tuple of
            value(str) if key is available None if key is not available
            message(str)
        '''
        key = str(key)
        if not is_valid_key(key):
            return None, 'invalid key'
        data_json = requests.post(self._address + 'get', json={'KEY': key}).json()
        return data_json['value'], data_json['message']
    
    def set(self, key: str, value: str, ttl: int = None) -> (Tuple[bool, str]):
        '''
        Method for setting values (SET)
        ttl - live time in seconds

        Returns: Tuple of
            is_created - True(bool) if can create or update value by key, or False if can not
            message - str
        '''
        key = str(key)
        value = str(value)
        if not is_valid_key(key):
            return False, 'invalid key'
        query = {
            'KEY': key,
            'VALUE': value
        }
        if ttl is not None:
            query['TTL'] = int(ttl)
        data_json = requests.post(self._address + 'set', json=query).json()
        return data_json['is_created'], data_json['message']
    
    def lset(self, key: str, value: List[str], ttl: int = None) -> (bool):
        '''
        Method for setting lists of values (SET)
        ttl - live time in seconds

        Returns: Tuple of
            is_created: True(bool) if can create or update list by key, or False if can not
            message: (str) error or ok message
        '''
        key = str(key)
        value = list(map(str, value))
        if not is_valid_key(key):
            return False, 'invalid key'
        query = {
            'KEY': key,
            'VALUE': value
        }
        if ttl is not None:
            query['TTL'] = int(ttl)

        data_json = requests.post(self._address + 'lset', json=query).json()
        return data_json['is_created'], data_json['message']

    def lget(self, key: str) -> (List[str]):
        '''
        Method for getting values by key (GET)

        Returns: 
        values lists(list of str) if key is available
        None if key is not available
        '''
        key = str(key)
        if not is_valid_key(key):
            return None
        data_json = requests.post(self._address + 'lget', json={'KEY': key}).json()
        return data_json['value'], data_json['message']

    def keys(self) -> (List[str]):
        '''
        Method for getting keys list (KEYS)

        Returns:
            keys: List of str
        '''
        return requests.get(self._address+'keys').json()['keys']

    def delete(self, key) -> (Tuple[bool, str]):
        '''
        Method for deleting key (DEL)

        Returns: Tuple of
            is_deleted: (bool) True if deleted and False if didn't deleted
            message: (str) ERROR or Ok message
        '''
        if not is_valid_key(key):
            return False, 'invalid key'
        data_json = requests.delete(self._address + 'del', json={'KEY': key}).json()
        return data_json['is_deleted'], data_json['message']