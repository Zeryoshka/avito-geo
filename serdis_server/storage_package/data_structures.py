'''
Description of data stuctures imlemented in project
'''

from datetime import datetime, timedelta


class Value():
    '''
    Base value stored in storage
    '''

    def __init__(self, value: str, ttl: int) -> (None):
        '''
        Create new value and set ttl if it isn't None
        '''
        self._value = value
        if ttl is None:
            self.ttl = False
        else:
            self.ttl = True
            self._time_of_dead = datetime.now() + timedelta(seconds=ttl)

    @property
    def value(self) -> (int):
        '''
        getting value of Value
        '''
        if self.is_alive:
            return self._value
        return None

    @property
    def is_alive(self) -> (bool):
        '''
        Checking value for aliving
        '''
        if self.ttl:
            return self._time_of_dead > datetime.now()
        return True


class ValueList():
    '''
    list of values stored in storage
    '''

    def __init__(self, value: str, ttl: int) -> (None):
        '''
        Create new value list and set ttl if it isn't None
        '''
        self._value = value
        if ttl is None:
            self.ttl = False
        else:
            self.ttl = True
            self._time_of_dead = datetime.now() + timedelta(seconds=ttl)

    @property
    def value(self) -> (int):
        '''
        getting value of ValueList
        '''
        if self.is_alive:
            return self._value
        return None

    @property
    def is_alive(self) -> (bool):
        '''
        Checking value list for aliving
        '''
        if self.ttl:
            return self._time_of_dead > datetime.now()
        return True
