#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Copyright 2017 Savin Mihael
# Simple Twitter search with you hashtag

import random
import datetime
import time
import twitter
import hackerutils


LOG_FILE_PATH = hackerutils.get_log_path('twit-excuse.log')

# Twitter credential
TOKEN = "348461715-xHvVlvAngLpnrusAnGPt0YW8Iq091QRAp6zjNL1A"
TOKEN_KEY = "1VyZ3hfKGs0RjLIeIbaBT85rroyryzIHCP7zKQOqplqWk"
CON_SEC = "KaZWD1NVIkiIchGBw8dWOo9Q4"
CON_SEC_KEY = "XEg3LAdw2KsZu4iR0vWusmNKbGtxx41vB8uCSi8hbDIsIpaIcW"


def main():
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    my_auth = twitter.OAuth(TOKEN, TOKEN_KEY, CON_SEC, CON_SEC_KEY)
    twit = twitter.Twitter(auth=my_auth)

    reasons = [
        'Много работы',
        'Надо доделать компьютер сотруднику',
        'Кто-то снова сломал сервер',
        'У нас проверка',
        'Я на совещании',
        'Я на встрече',
        'Ничего не успеваю',
        'Я задерживаюсь в офисе',
        'Я настраиваю новую систему',
        'Буду поздно',
    ]

    try:
        tweet = random.choice(reasons) + ' ' + date
        twit.statuses.update(status=tweet)
        with LOG_FILE_PATH.open('a') as f:
            f.write('Done: {}'.format(tweet) + '\n\r')
    except Exception as e:
        # Log errors.
        with LOG_FILE_PATH.open('a') as f:
            f.write('Failed to send twit: {}'.format(e))
        raise

    return


if __name__ == '__main__':
    main()
