'''
Client for python serdis database
'''
from typing import List
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
        self.adress = f'http://{host}:{port}/'
    
    def get(self, key: str) -> (str):
        '''
        Method for getting values by key (GET)

        Returns: 
        value(str) if key is available
        None if key is not available
        '''
        key = str(key)
        if not is_valid_key(key):
            return None
        value = requests.post(self.adress + 'get', json={'KEY': key}).json()['value']
        return value
    
    def set(self, key: str, value: str, ttl: int = None) -> (bool):
        '''
        Method for setting values (SET)
        ttl - live time in seconds

        Returns:
        True(bool) if can create or update value by key, or False if can not
        '''
        key = str(key)
        value = str(value)
        if not is_valid_key(key):
            return False
        query = {
            'KEY': key,
            'VALUE': value
        }
        if ttl is not None:
            query['TTL'] = int(ttl)
        is_created = requests.post(self.adress + 'set', json=query).json()['is_created']
        return is_created
    
    def lset(self, key: str, value: List[str], ttl: int = None) -> (bool):
        '''
        Method for setting lists of values (SET)
        ttl - live time in seconds

        Returns:
        True(bool) if can create or update list by key, or False if can not
        '''
        key = str(key)
        value = list(value)
        if not is_valid_key(key):
            return False
        query = {
            'KEY': key,
            'VALUE': value
        }
        if ttl is not None:
            query['TTL'] = int(ttl)

        is_created = requests.post(self.adress + 'lset', json=query).json()['is_created']
        return is_created

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
        value = requests.post(self.adress + 'lget', json={'KEY': key}).json()['value']
        return value