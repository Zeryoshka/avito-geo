from serdis_server import app, storage
from serdis_server.handlers.headers import HEADERS
import pytest
import json
from time import sleep


@pytest.fixture()
def client():
    storage.__init__()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_pong(client):
    resp = client.get('/ping')
    status, data = resp.status_code, resp.get_data().decode()
    assert data == 'PONG' and status == 200

def test_get_and_set(client):
    resp = client.post(
        '/set', 
        data=json.dumps({
            'KEY': 'key1',
            'VALUE': 'value1'
        }), 
        headers=HEADERS
    )
    status, data = resp.status_code, resp.get_json()
    assert data['is_created'] and status == 201
    
    resp = client.post(
        '/set', 
        data=json.dumps({
            'KEY': '2key',
            'VALUE': 'val1'
        }), 
        headers=HEADERS
    )
    status, data = resp.status_code, resp.get_json()
    assert status == 400 and not data['is_created']

    resp = client.post(
        '/get', 
        data=json.dumps({
            'KEY': '2key',
        }), 
        headers=HEADERS
    )
    status, data = resp.status_code, resp.get_json()
    assert status == 400 and data['value'] is None

    resp = client.post(
        '/get', 
        data=json.dumps({
            'KEY': 'key1',
        }), 
        headers=HEADERS
    )
    status, data = resp.status_code, resp.get_json()
    assert status == 200 and data['value'] == 'value1'

def test_get_and_set_ttl(client):
    resp = client.post(
        '/set', 
        data=json.dumps({
            'KEY': 'key1',
            'VALUE': 'value1',
            'TTL': 2
        }), 
        headers=HEADERS
    )
    status, data = resp.status_code, resp.get_json()
    assert data['is_created'] and status == 201
    
    resp = client.post(
        '/get', 
        data=json.dumps({
            'KEY': 'key1',
        }), 
        headers=HEADERS
    )
    status, data = resp.status_code, resp.get_json()
    assert status == 200 and data['value'] == 'value1'

    sleep(2)
    
    resp = client.post(
        '/get', 
        data=json.dumps({
            'KEY': 'key1',
        }), 
        headers=HEADERS
    )
    status, data = resp.status_code, resp.get_json()
    assert data['value'] is None and status == 400

def test_lset_and_lget(client):
    
    resp = client.post(
        '/lset', 
        data=json.dumps({
            'KEY': 2,
            'VALUE': 'val1'
        }), 
        headers=HEADERS
    )
    status, data = resp.status_code, resp.get_json()
    assert status == 400 and not data['is_created']

    resp = client.post(
        '/lget', 
        data=json.dumps({
            'KEy': 'key2',
            'VALUE': 'val1'
        }), 
        headers=HEADERS
    )
    status, data = resp.status_code, resp.get_json()
    assert status == 400 and data['value'] is None

    resp = client.post(
        '/lset', 
        data=json.dumps({
            'KEY': 'key1',
            'VALUE': ['value1', 'value2', 'value3']
        }), 
        headers=HEADERS
    )
    status, data = resp.status_code, resp.get_json()
    assert data['is_created'] and status == 201
    
    resp = client.post(
        '/lset', 
        data=json.dumps({
            'KEY': 'key1',
            'VALUE': ['value1', 'value2', 'value3']
        }), 
        headers=HEADERS
    )
    status, data = resp.status_code, resp.get_json()
    assert data['is_created'] and status == 201
    
    resp = client.post(
        '/lget', 
        data=json.dumps({
            'KEY': 'key2',
        }), 
        headers=HEADERS
    )
    status, data = resp.status_code, resp.get_json()
    assert data['value'] is None and status == 400

    resp = client.post(
        '/lget', 
        data=json.dumps({
            'KEY': 'key1',
        }), 
        headers=HEADERS
    )
    status, data = resp.status_code, resp.get_json()
    assert data['value'] == ['value1', 'value2', 'value3'] and status == 200

def test_lset_and_lget_ttl(client):
    resp = client.post(
        '/lset', 
        data=json.dumps({
            'KEY': 'key1',
            'VALUE': ['value1', 'value2', 'value3'],
            'TTL': 2
        }), 
        headers=HEADERS
    )
    status, data = resp.status_code, resp.get_json()
    assert data['is_created'] and status == 201

    resp = client.post(
        '/lget', 
        data=json.dumps({
            'KEY': 'key1',
        }), 
        headers=HEADERS
    )
    status, data = resp.status_code, resp.get_json()
    assert data['value'] == ['value1', 'value2', 'value3'] and status == 200

    sleep(2)

    resp = client.post(
        '/lget', 
        data=json.dumps({
            'KEY': 'key1',
        }), 
        headers=HEADERS
    )
    status, data = resp.status_code, resp.get_json()
    assert data['value'] is None and status == 400

def test_keys(client):
    true_keys = []
    resp = client.get('/keys')
    status, data = resp.status_code, resp.get_json()
    assert status == 200 and set(data['keys']) == set(true_keys)
    
    for i in range(5):
        client.post(
            '/set', 
            data=json.dumps({
                'KEY': f'key{i}',
                'VALUE': str(i)
            }), 
            headers=HEADERS
        )
        true_keys.append(f'key{i}')
    resp = client.get('/keys')
    status, data = resp.status_code, resp.get_json()
    assert status == 200 and set(data['keys']) == set(true_keys)
    
    resp = client.post(
        '/set', 
        data=json.dumps({
            'KEY': 'key5',
            'VALUE': '5',
            'TTL': 2,
        }), 
        headers=HEADERS
    )
    true_keys.append('key5')
    resp = client.get('/keys')
    status, data = resp.status_code, resp.get_json()
    assert status == 200 and set(data['keys']) == set(true_keys)

    sleep(2)
    del true_keys[-1]
    resp = client.get('/keys')
    status, data = resp.status_code, resp.get_json()
    assert status == 200 and set(data['keys']) == set(true_keys)

def test_del(client):

    resp = client.get('/keys')
    _, data = resp.status_code, resp.get_json()

    true_keys = []
    for i in range(4):
        client.post(
            '/set', 
            data=json.dumps({
                'KEY': f'key{i}',
                'VALUE': str(i)
            }), 
            headers=HEADERS
        )
        true_keys.append(f'key{i}')

    resp = client.delete(
        '/del',
        data=json.dumps({
            'KEY': 'key1'
        }),
        headers=HEADERS
    )
    status_del, deleted = resp.status_code, resp.get_json()['is_deleted']
    del true_keys[1]
    resp = client.get('/keys')
    _, data = resp.status_code, resp.get_json()
    assert deleted and status_del == 200 and set(data['keys']) == set(true_keys)

    resp = client.delete(
        '/del',
        data=json.dumps({
            'KEY': 'key1'
        }),
        headers=HEADERS
    )
    status_del, deleted = resp.status_code, resp.get_json()['is_deleted']
    assert status_del == 400 and not deleted

    resp = client.delete(
        '/del',
        data=json.dumps({
            'KeY': 'key1'
        }),
        headers=HEADERS
    )
    status_del, deleted = resp.status_code, resp.get_json()['is_deleted']
    assert status_del == 400 and not deleted