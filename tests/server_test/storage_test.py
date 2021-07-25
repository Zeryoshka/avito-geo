from time import sleep
import pytest
from serdis_server.storage_package import Storage

@pytest.fixture
def storage():
    return Storage()

def test_storage_set_and_get(storage):
    created, _ = storage.set('key1', 'value1')
    assert created
    value, _ = storage.get('key1')
    assert value == 'value1'

def test_storage_many_set_and_get(storage):
    created, _ = storage.set('key1', 'value1')
    assert created
    created, _ = storage.set('key2', 'value2')
    assert created
    value, _ = storage.get('key1')
    assert value == 'value1'
    value, _ = storage.get('key2')
    assert value == 'value2'
    created, _ = storage.set('key1', 'value5')
    assert created
    value, _ = storage.get('key1')
    assert value == 'value5'
    value, _ = storage.get('key3')
    assert value is None

def test_storage_many_set_and_get_with_tll(storage):
    created, _ = storage.set('key1', 'value1', 3)
    assert created
    created, _ = storage.set('key2', 'value2', 2)
    assert created

    value, _ = storage.get('key1')
    assert value == 'value1'

    value, _ = storage.get('key2')
    assert value == 'value2'

    sleep(3)

    value, _ = storage.get('key1')
    assert value is None
    value, _ = storage.get('key2')
    assert value is None

def test_storage_lset_and_lget(storage):
    created, _ = storage.lset('key1', ['value1', 'value2', 'value3', 'value4'])
    assert created
    value, _ = storage.get('key2')
    assert value is None
    value, _ = storage.lget('key1')
    assert value == ['value1', 'value2', 'value3', 'value4']

def test_storage_lset_and_lget_ttl(storage):
    created, _ = storage.lset('key1', ['value1', 'value2', 'value3', 'value4'], 1)
    assert created
    value, _ = storage.lget('key1')
    assert value == ['value1', 'value2', 'value3', 'value4']
    sleep(2);
    value, _ = storage.lget('key1')
    assert value is None

def test_storage_combi_set(storage):
    created, _ = storage.lset('key1', ['1', '2', '3', '4'])
    assert created
    created, _ = storage.set('key1', '23')
    assert not created
    value, _ = storage.get('key1')
    assert value is None

def test_storage_keys(storage):
    true_keys = []
    for i in range(3):
        storage.set(f'key{i}', f'{i}')
        true_keys.append(f'key{i}')
    storage.lset('list', ['1', '2', '3'])
    true_keys.append('list')

    keys = storage.keys()
    assert set(keys) == set(true_keys)
    storage.set('key4', '4', 2)
    true_keys.append('key4')
    keys = storage.keys()
    assert set(keys) == set(true_keys)
    sleep(2)
    del true_keys[-1]
    keys = storage.keys()
    assert set(keys) == set(true_keys)

def test_storage_delete(storage):
    true_keys = []
    for i in range(10):
        storage.set(f'key{i}', f'{i}')
        true_keys.append(f'key{i}')
    
    deleted, _ = storage.delete('key9')
    del true_keys[-1]
    assert deleted and set(storage.keys()) == set(true_keys)

    deleted, _ = storage.delete('key10')
    assert not deleted and set(storage.keys()) == set(true_keys)

    storage.set('key10', '10', 1)
    sleep(1)
    deleted, _ = storage.delete('key10')
    assert not deleted and set(storage.keys()) == set(true_keys)


