'''
CLI client for serdis
'''
from typing import List
from . import Serdis

a = f''

client = Serdis()


def ping_command(parametrs: List[str]) -> (None):
    if len(parametrs) > 0:
        print('''
            PARAMETRS ERROR
            must be 0 parametrs
        ''')
        return
    print(client.ping())

def set_command(parametrs: List[str]) -> (None):
    if 1 >= len(parametrs) <= 3:
        print('''
            PARAMETRS ERROR
            must be 2 or 3 parametrs
        ''')
        return
    ttl = None
    if len(parametrs) == 3:
        if not parametrs[2].isdigit():
            print('''
                PARAMETRS ERROR
                third parametr must be numeric
            ''')
            return
        ttl = int(parametrs[2])
    is_created, message = client.set(parametrs[0], parametrs[1], ttl)
    if not is_created:
        print(f'''
            ERROR:
            {message}
        ''')
    else:
        print(message)

def exit_command(parametrs: List[str]) -> (bool):
    if len(parametrs) > 0:
        print('''
            PARAMETRS ERROR
            must be 0 parametrs
        ''')
        return False
    return True

def get_command(parametrs: List[str]) -> (None):
    if len(parametrs) != 1:
        print('''
            PARAMETRS ERROR
            must be 1 parametr
        ''')
        return
    value, message = client.get(parametrs[0])
    if value is None:
        print(f'''
            ERROR:
            {message}
        ''')
        return
    print(value)

def keys_command(parametrs: List[str]) -> (None):
    if parametrs != []:
        print('''
            PARAMETRS ERROR
            must be 0 parametrs
        ''')
        return
    values = client.keys()
    print(len(values), ': ', ', '.join(values), ';', sep='')

def del_command(parametrs: List[str]) -> (None):
    if len(parametrs) != 1:
        print('''
            PARAMETRS ERROR
            must be 1 parametr
        ''')
        return
    is_deleted, message = client.delete(parametrs[0])
    if not is_deleted:
        print(f'''
            ERROR:
            {message}
        ''')
    else:
        print(message)

def lset_command(parametres: List[str]) -> (None):
    if 1 >= len(parametrs) <= 3:
        print('''
            PARAMETRS ERROR
            must be 2 or 3 parametrs
        ''')
        return
    ttl = None
    if len(parametrs) == 3:
        if not parametrs[2].isdigit():
            print('''
                PARAMETRS ERROR
                third parametr must be numeric
            ''')
            return
        ttl = int(parametrs[2])
    
    is_created, message = client.lset(parametrs[0], parametrs[1], ttl)
    if not is_created:
        print(f'''
            ERROR:
            {message}
        ''')
    else:
        print(message)


while True:
    print('>>> ', end='')
    splited_line = input().split()
    if splited_line == []:
        continue
    command, parametrs = splited_line[0].upper(), splited_line[1:]
    
    if command == 'PING':
        ping_command(parametrs)
    elif command == 'GET':
        get_command(parametrs)
    elif command == 'SET':
        set_command(parametrs)
    elif command == 'KEYS':
        keys_command(parametrs)
    elif command == 'DEL':
        del_command(parametrs)
    elif command == 'LSET':
        lset_command(parametrs)
    elif command == 'LGET':
        pass
    elif command == 'EXIT':
        if exit_command(parametrs):
            break
    else:
        print('UNKNOWN COMMAND')