'''
Init module of storage package
'''

from typing import Any, List, Tuple

from .data_structures import Value, ValueList


class Storage():
    '''
    Storage class holding all information
    '''

    def __init__(self):
        '''
        Create new storage object
        '''
        self._values = dict()

    def _is_key_exist_for_other_type(self, key: str, type_: type) -> (bool):
        '''
        Return True if key already exist for other data structure
        '''
        return (
            key in self._values and
            not isinstance(self._values[key], type_)
        )

    def _get_validator(self, key: str, type_: type) -> (Tuple[Any, str]):
        '''
        Validator get-requests(GET, LGET, HGET)

        Returns:
            Value - Value of type_ or None
            Message - str
        '''
        if key not in self._values:
            return None, 'Key is not exist'
        value = self._values[key]
        if not value.is_alive:
            del self._values[key]
            return None, 'Key is not exist'
        if not isinstance(value, type_):
            return None, 'Value mismatch'
        return value.value, 'Ok'

    def set(self, key: str, value: str, ttl: int = None) -> (Tuple[bool, str]):
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

        self._values[key] = Value(value, ttl)
        return True, 'Ok'

    def get(self, key: str) -> (Tuple[str, str]):
        '''
        Get Value by key if it's exist and alive
        If key is not exist, is not alive or has mismatch in type returns None

        Returns:
            value - str or None
            message - str
        '''
        return self._get_validator(key, Value)

    def lset(
        self, key: str, value: str, ttl: int = None
    ) -> (Tuple[bool, str]):
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

        self._values[key] = ValueList(value, ttl)
        return True, 'Ok'

    def lget(self, key: str) -> (Tuple[List[str], str]):
        '''
        set List by key, make pair key-value in storage,
        can set TTL if ttl not is None

        if key uses for other type of datastructure returns errors message

        Returns: tuple with
            value - list of str or None
            message - str
        '''
        return self._get_validator(key, ValueList)

    def keys(self) -> (List[str]):
        '''
        get all keys and return it.

        Returns:
            list of str with keys
        '''
        keys = []
        for key, value in list(self._values.items()):
            if value.is_alive:
                keys.append(key)
            else:
                del self._values[key]
                print(self._values.keys())
        return keys

    def delete(self, key: str) -> (Tuple[bool, str]):
        '''
        del key if it exists
        Returns:
            is_deleted - (bool) True if deleted
            message - str
        '''
        if key in self._values:
            if self._values[key].is_alive:
                del self._values[key]
                return True, 'Ok'
            del self._values[key]
        return False, 'Key is not exist'
