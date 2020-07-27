# refer: https://docs.python.org/3/howto/logging.html#logging-advanced-tutorial

import logging
import sys


# Multiple calls to logging.getLogger('someLogger') return a
# reference to the same logger object.  This is true not only
# within the same module, but also across modules as long as
# it is in the same Python interpreter process.

FORMATTER = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s —" "%(funcName)s:%(lineno)d — %(message)s"  #datetime stamp , name of the logger , levelname , name of the function from which the log was generated , line number within the function , the actual message that we logged.
)


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout) # logs will be shown on the terminal, alternatively we could have assigned a file handler where the logs would have been sent to a file.
    console_handler.setFormatter(FORMATTER)
    return console_handler
