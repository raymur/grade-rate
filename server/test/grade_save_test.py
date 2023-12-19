from flask import Flask
import pytest
from grade_save.app import create_app
import time


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client
            
def test_ping(client):
    rv = client.get('/ping')
    assert rv.get_data() == b'pong'


def test_add_grade(client):
    rv = client.post('/add_route')
    assert rv.get_data()
    route_id = rv.get_data().decode("utf-8")
    print(route_id)
    client.post('/add_grade/' + route_id, json={"grade": "v1"})
    client.post('/add_grade/' + route_id, json={"grade": "v2"})
    client.post('/add_grade/' + route_id, json={"grade": "v3"})
    rv = client.get('/generate_average/' + route_id)
    assert rv.get_data() == b'v2'