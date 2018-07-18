#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Copyright 2017 Savin (JTProg) Mihael
# Simple Twitter posting excuse
# https://jtprog.ru/

import twitter
import dotenv as d
from pathlib import Path
import logging
import os
import utils

# Get current working directory
cwd = os.path.dirname(os.path.abspath(__file__))
# Log file name
LOG_FILE_PATH = cwd + '/logs/info.log'

logging.getLogger(__name__)
# Logging configuration
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d]# \
%(levelname)s [%(asctime)s]  %(message)s',
                    level=logging.DEBUG,
                    filename=LOG_FILE_PATH)

# Twitter credential
env = str(Path(__file__).parent / '.env')

try:
    TOKEN = d.get_variable(env, 'TOKEN')
    TOKEN_KEY = d.get_variable(env, 'TOKEN_KEY')
    CON_SEC = d.get_variable(env, 'CON_SEC')
    CON_SEC_KEY = d.get_variable(env, 'CON_SEC_KEY')
except Exception as e:
    # Log errors.
    logging.fatal(u'Can\'t get configuration from enviroment\n\nFATAL: {}'.format(e))


def main():
    my_auth = twitter.OAuth(TOKEN, TOKEN_KEY, CON_SEC, CON_SEC_KEY)
    # List of a reasons
    reasons = utils.get_excuse()

    try:
        twit = twitter.Twitter(auth=my_auth)
        # Send tweet
        # tweet = random.choice(reasons)
        twit.statuses.update(status=reasons[0:139])
        logging.info(u'INFO: {}'.format('Message send'))
    except Exception as e:
        # Log errors
        logging.fatal(u'FATAL: {}'.format(e))

    return


if __name__ == '__main__':
    main()
