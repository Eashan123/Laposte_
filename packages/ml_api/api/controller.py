from flask import Blueprint, request, jsonify
from api.config import get_logger
from le_poste import __version__ as _version

from le_poste.trained_models.predict import make_prediction
from api import __version__ as api_version

_logger = get_logger(logger_name=__name__)

prediction_app = Blueprint('prediction_app', __name__)


@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        _logger.info('health status OK')
        return 'healthy running'

@prediction_app.route('/version', methods=['GET'])
def version():
    if request.method == 'GET':
        return jsonify({'model_version': _version,
                        'api_version': api_version})

# @prediction_app.route('/v1/predict/regression', methods=['POST'])
# Thing to note is that no feature engineering adjustments going on within the api, the job of prediction is mostly on the
# leposte package because. We are seperating concerns and keep our api as light as possible.


@prediction_app.route('/v1/predict/le_poste', methods=['POST'])
def predict():
    if request.method == 'POST':
        json_data = request.get_json()
        _logger.info(f'Inputs: {json_data}')

        result = make_prediction(input_data=json_data)
        _logger.info(f'Outputs: {result}')

        predictions = result.get('predictions')[0]
        version = result.get('version')

        return jsonify({'predictions': predictions,
                        'version': version})