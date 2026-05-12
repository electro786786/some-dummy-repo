import logging

logger = logging.getLogger(__name__)

def log_info_message(message):
    logger.info(message)

def log_error_message(message):
    logger.error(message)
