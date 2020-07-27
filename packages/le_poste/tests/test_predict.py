import math

from le_poste.trained_models.predict import make_prediction
from le_poste.processing.data_management import load_dataset
from le_poste.config import config


def test_make_prediction():
    # Given
    test_data = load_dataset(file_name=config.TESTING_DATA_FILE)
    original_data_length = len(test_data)
    test_json = test_data.to_json(orient='records', force_ascii = False)

    # When
    subject = make_prediction(input_data=test_json)

    # Then
    assert subject is not None
    assert isinstance(subject.get('predictions')[0], str)
    assert len(subject.get('predictions')) == original_data_length
