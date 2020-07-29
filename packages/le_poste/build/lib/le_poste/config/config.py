#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pathlib

import le_poste
import pandas as pd

PACKAGE_ROOT = pathlib.Path(le_poste.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / "models"
DATASET_DIR = PACKAGE_ROOT / "data"
ENTITY_DIR = PACKAGE_ROOT / "entity"

TESTING_DATA_FILE = "test.xlsx"
TRAINING_DATA_FILE = "train.xlsx"

ENTITY_FILE = "MESSI_Extraction.xlsx"

pd.options.display.max_rows = 10
pd.options.display.max_columns = 10

# pipeline name
PIPELINE_NAME = 'Random_Forest'
PIPELINE_SAVE_FILE = f"{PIPELINE_NAME}_output_v"

# features
FEATURES = 'Résumé'

# target
TARGET = 'SubCat Translated'

# drop features
DROP_F = 'Unnamed: 0'

# entity name
ENTITY_NAME = 'Extracted_Entity'
ENTITY_SAVE_FILE = f"{ENTITY_NAME}_output_v"

MANUAL_ENTITY = 'Manual_Queue'
MANUALEn_SAVE_FILE = f"{MANUAL_ENTITY}_output_v"

# # entity save directory
# path_s = ENTITY_DIR

CAT = "Demande de déploiement"

CAT_NOT_NA = ['SubCat Translated']

# used for differential testing
ACCEPTABLE_MODEL_DIFFERENCE = 0.05






