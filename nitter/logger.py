"""

logger module
"""
import logging


def configure_logger(level: int = logging.DEBUG) -> logging.Logger:
    """

    configure logger
    :param level:
    :return:
    """
    logger = logging.getLogger("nitter")
    logger.setLevel(level)

    # create console handler and set level to debug
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to console_handler
    console_handler.setFormatter(formatter)

    # add console_handler to logger
    logger.addHandler(console_handler)

    return logger
