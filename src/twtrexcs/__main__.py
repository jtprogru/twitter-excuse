#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2017 Savin (JTProg) Mihael
# Simple Twitter posting excuse
# https://jtprog.ru/
"""
Main module of twtrexcs
"""


import logging
import os

import twitter

from twtrexcs.helpers import get_excuse


class TwtrExcsException(Exception):
    pass


class CustomFormatter(logging.Formatter):
    """
    Colored Formatter for logging
    """

    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format_string = "%(asctime)s - %(name)s - %(levelname)s - (%(filename)s:%(lineno)d) - %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format_string + reset,
        logging.INFO: grey + format_string + reset,
        logging.WARNING: yellow + format_string + reset,
        logging.ERROR: red + format_string + reset,
        logging.CRITICAL: bold_red + format_string + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create console handler with a higher log level
fh = logging.FileHandler(os.getenv("LOG_FILE_PATH", "twitterbot.log"))
fh.setLevel(logging.DEBUG)

fh.setFormatter(CustomFormatter())

logger.addHandler(fh)


def main() -> None:
    TOKEN = os.getenv("TOKEN", None)
    TOKEN_KEY = os.getenv("TOKEN_KEY", None)
    CON_SEC = os.getenv("CON_SEC", None)
    CON_SEC_KEY = os.getenv("CON_SEC_KEY", None)
    if TOKEN is None:
        # Log errors.
        logger.error("Can't get TOKEN from environment")
    else:
        logger.info("TOKEN is loaded from environment")

    # Authorisation in Twitter
    my_auth = twitter.OAuth(TOKEN, TOKEN_KEY, CON_SEC, CON_SEC_KEY)

    # get a reason's
    reason = get_excuse()
    logger.info(u"INFO: Status for Twitter is: %s", reason)

    logger.info(u"INFO: %s", "Try to login")
    try:
        twit = twitter.Twitter(auth=my_auth)
        # Send tweet
        logger.info(u"INFO: %s", "Try to send message")
        twit.statuses.update(status=reason)
        logger.info(u"INFO: %s", "Message ->")
        logger.info(u"MESSAGE: %s", reason)
        logger.info(u"INFO: %s", "...is sended")
    except TwtrExcsException as e:
        # Log errors
        logger.error(u"FATAL: %s", e)


if __name__ == "__main__":
    main()
