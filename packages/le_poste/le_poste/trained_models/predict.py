import numpy as np
import pandas as pd
#from le_poste.entity_extraction.extraction.extraction_ import Entity_Extraction
from le_poste.processing.data_management import load_pipeline
from le_poste.config import config
from le_poste.processing import validation
# from le_poste.trained_models.manual_queue import  Queue
from le_poste import __version__ as _version
import logging

_logger = logging.getLogger(__name__)

pipeline_file_name = f"{config.PIPELINE_SAVE_FILE}{_version}.pkl"
_category_pipe = load_pipeline(file_name=pipeline_file_name)



def make_prediction(*, input_data) -> dict:
    """Make a prediction using the saved model pipeline."""

    data = pd.read_json(input_data)
    validated_data = validation.validate_inputs(input_data=data)  #This will perform filtering before passing data into pipeline
    prediction = _category_pipe.predict(validated_data[[config.FEATURES]])
    response = {'predictions': prediction, "version": _version}
    
    _logger.info(
        f"Making predictions with model version: {_version} "
        f"Inputs: {validated_data} "
        f"Predictions: {response}"
    )
    
 
    return response
