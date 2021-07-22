from serdis_server.storage_package.data_structures import Value
from serdis_server.storage_package import Storage
from time import sleep

def test_storage_set_and_get():
    storage = Storage()
    created, _ = storage.set('key1', 'value1')
    assert created
    value, _ = storage.get('key1')
    assert value == 'value1'

def test_storage_many_set_and_get():
    storage = Storage()
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

def test_storage_many_set_and_get_with_tll():
    storage = Storage()
    
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

def test_storage_lset_and_lget():
    storage = Storage()
    created, _ = storage.lset('key1', ['value1', 'value2', 'value3', 'value4'])
    assert created
    value, _ = storage.get('key2')
    assert value is None
    value, _ = storage.lget('key1')
    assert value == ['value1', 'value2', 'value3', 'value4']

def test_storage_lset_and_lget_ttl():
    storage = Storage()
    created, _ = storage.lset('key1', ['value1', 'value2', 'value3', 'value4'], 1)
    assert created
    value, _ = storage.lget('key1')
    assert value == ['value1', 'value2', 'value3', 'value4']
    sleep(2);
    value, _ = storage.lget('key1')
    assert value is None

def test_storage_combi_set():
    storage = Storage()
    created, _ = storage.lset('key1', ['1', '2', '3', '4'])
    assert created
    created, _ = storage.set('key1', '23')
    assert not created
    value, _ = storage.get('key1')
    assert value is None
