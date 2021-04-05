#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2017 Savin (JTProg) Mihael
# Simple Twitter posting excuse
# https://jtprog.ru/

import twitter
import logging
import os
import utils


class CustomFormatter(logging.Formatter):
    """
    Colored Formatter for logging
    """
    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

ch.setFormatter(CustomFormatter())

logger.addHandler(ch)


def main() -> None:
    TOKEN = os.getenv("TOKEN", None)
    TOKEN_KEY = os.getenv('TOKEN_KEY', None)
    CON_SEC = os.getenv('CON_SEC', None)
    CON_SEC_KEY = os.getenv('CON_SEC_KEY', None)
    if TOKEN is None:
        # Log errors.
        logger.fatal("Can't get TOKEN from environment")

    # Authorisation in Twitter
    my_auth = twitter.OAuth(TOKEN, TOKEN_KEY, CON_SEC, CON_SEC_KEY)
    # List of a reason's
    reason = utils.get_excuse()

    try:
        twit = twitter.Twitter(auth=my_auth)
        # Send tweet
        twit.statuses.update(status=reason[0:139])
        logging.info(u'INFO: {}'.format('Message \"' + reason[0:139] + '\" send'))
    except Exception as e:
        # Log errors
        logging.fatal(u'FATAL: {}'.format(e))


if __name__ == '__main__':
    main()

