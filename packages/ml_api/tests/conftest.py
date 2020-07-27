import pytest
import sys, os

#https://stackoverflow.com/questions/38231478/why-is-relative-path-not-working-in-python-tests

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))

sys.path.insert(0, PROJECT_DIR)

import api
from api.app import create_app
from api.config import TestingConfig


@pytest.fixture
def app():
    app = create_app(config_object=TestingConfig)

    with app.app_context():
        yield app


@pytest.fixture
def flask_test_client(app):
    with app.test_client() as test_client:
        yield test_client