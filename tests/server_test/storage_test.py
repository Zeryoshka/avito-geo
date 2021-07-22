from serdis_server.storage_package import Storage


def test_storage_test1():
    storage = Storage()
    
    created, message = storage.set('key1', 'value1')
    assert created
