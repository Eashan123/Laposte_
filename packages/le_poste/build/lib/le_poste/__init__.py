import logging

from le_poste.config import config
from le_poste.config import logging_config


VERSION_PATH = config.PACKAGE_ROOT / 'VERSION'

# Configure logger for use in package
logger = logging.getLogger(__name__)  # __name__ will equate to le_poste
logger.setLevel(logging.DEBUG)
logger.addHandler(logging_config.get_console_handler())
logger.propagate = False


with open(VERSION_PATH, 'r') as version_file:
    __version__ = version_file.read().strip()  # __ is the quazi standard of python.
    
# Now we are ready to call our logger in our individual modules.
