import logging

from inet import *
#from inet.simulation.cffi import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setFormatter(ColoredLoggingFormatter())

logger.handlers = []
logger.addHandler(handler)

enable_autoreload()

print("INET python support is loaded.")
