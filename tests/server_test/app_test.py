import pytest
import json
from time import sleep
from serdis_server import app


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_pong(client):
    resp = client.get('/ping')
    status = resp.status
    data = resp.get_data().decode()
    assert data == 'PONG'

def test_pong(client):
    resp = client.get('/ping')
    status = resp.status_code
    data = resp.get_data().decode()
    assert data == 'PONG' and status == 200

def test_get_and_set(client):
    resp = client.post(
        '/set', 
        data=json.dumps({
            'KEY': 'key1',
            'VALUE': 'value1'
        }), 
        headers={
            'Content-Type': 'application/json'
        }
    )
    status, data = resp.status_code, resp.get_json()
    assert data['is_created'] and status == 201
    
    resp = client.post(
        '/set', 
        data=json.dumps({
            'KEY': '2key',
            'VALUE': 'val1'
        }), 
        headers={
            'Content-Type': 'application/json'
        }
    )
    status, data = resp.status_code, resp.get_json()
    assert status == 400 and not data['is_created']

    resp = client.post(
        '/get', 
        data=json.dumps({
            'KEY': '2key',
        }), 
        headers={
            'Content-Type': 'application/json'
        }
    )
    status, data = resp.status_code, resp.get_json()
    assert status == 400 and data['value'] is None

    resp = client.post(
        '/get', 
        data=json.dumps({
            'KEY': 'key1',
        }), 
        headers={
            'Content-Type': 'application/json'
        }
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
        headers={
            'Content-Type': 'application/json'
        }
    )
    status, data = resp.status_code, resp.get_json()
    assert data['is_created'] and status == 201
    
    resp = client.post(
        '/get', 
        data=json.dumps({
            'KEY': 'key1',
        }), 
        headers={
            'Content-Type': 'application/json'
        }
    )
    status, data = resp.status_code, resp.get_json()
    assert status == 200 and data['value'] == 'value1'

    sleep(2)
    
    resp = client.post(
        '/get', 
        data=json.dumps({
            'KEY': 'key1',
        }), 
        headers={
            'Content-Type': 'application/json'
        }
    )
    status, data = resp.status_code, resp.get_json()
    assert data['value'] is None and status == 400

def test_lset_and_lget(client):
    resp = client.post(
        '/lset', 
        data=json.dumps({
            'KEY': 'key1',
            'VALUE': ['value1', 'value2', 'value3']
        }), 
        headers={
            'Content-Type': 'application/json'
        }
    )
    status, data = resp.status_code, resp.get_json()
    assert data['is_created'] and status == 201
    
    resp = client.post(
        '/lset', 
        data=json.dumps({
            'KEY': 'key1',
            'VALUE': ['value1', 'value2', 'value3']
        }), 
        headers={
            'Content-Type': 'application/json'
        }
    )
    status, data = resp.status_code, resp.get_json()
    assert data['is_created'] and status == 201
    
    resp = client.post(
        '/lget', 
        data=json.dumps({
            'KEY': 'key2',
        }), 
        headers={
            'Content-Type': 'application/json'
        }
    )
    status, data = resp.status_code, resp.get_json()
    assert data['value'] is None and status == 400

    resp = client.post(
        '/lget', 
        data=json.dumps({
            'KEY': 'key1',
        }), 
        headers={
            'Content-Type': 'application/json'
        }
    )
    status, data = resp.status_code, resp.get_json()
    assert data['value'] == ['value1', 'value2', 'value3'] and status == 200

def test_lset_and_lget(client):
    resp = client.post(
        '/lset', 
        data=json.dumps({
            'KEY': 'key1',
            'VALUE': ['value1', 'value2', 'value3'],
            'TTL': 2
        }), 
        headers={
            'Content-Type': 'application/json'
        }
    )
    status, data = resp.status_code, resp.get_json()
    assert data['is_created'] and status == 201

    resp = client.post(
        '/lget', 
        data=json.dumps({
            'KEY': 'key1',
        }), 
        headers={
            'Content-Type': 'application/json'
        }
    )
    status, data = resp.status_code, resp.get_json()
    assert data['value'] == ['value1', 'value2', 'value3'] and status == 200

    sleep(2)

    resp = client.post(
        '/lget', 
        data=json.dumps({
            'KEY': 'key1',
        }), 
        headers={
            'Content-Type': 'application/json'
        }
    )
    status, data = resp.status_code, resp.get_json()
    assert data['value'] is None and status == 400