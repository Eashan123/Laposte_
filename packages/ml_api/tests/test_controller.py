from le_poste.config import config as model_config
from le_poste.processing.data_management import load_dataset
from le_poste import __version__ as _version
import os, sys


TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))

sys.path.insert(0, PROJECT_DIR)

import api
from api import __version__ as api_version

import pytest
import json
import math

#@pytest.mark.filterwarnings('ignore::RuntimeWarning')

def test_health_endpoint_returns_200(flask_test_client):
    # When
    response = flask_test_client.get('/health')

    # Then
    assert response.status_code == 200

def test_version_endpoint_returns_version(flask_test_client):
    # When
    response = flask_test_client.get('/version')

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json['model_version'] == _version
    assert response_json['api_version'] == api_version


def test_prediction_endpoint_returns_prediction(flask_test_client):
    # Given
    # Load the test data from the regression_model package
    # This is important as it makes it harder for the test
    # data versions to get confused by not spreading it
    # across packages.
    test_data = load_dataset(file_name=model_config.TESTING_DATA_FILE)

    # https://stackoverflow.com/questions/39612240/writing-pandas-dataframe-to-json-in-unicode
    post_json = test_data[0:10].to_json(orient='records', force_ascii=False)

    # When
    response = flask_test_client.post('/v1/predict/le_poste', json=post_json)

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)
    prediction = response_json['predictions']
    response_version = response_json['version']
#    assert math.ceil(prediction) == 112476
    assert response_version == _version