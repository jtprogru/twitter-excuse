# coding=utf-8
import random
from excuses.data import EXCUSES, HASHTAGS, SPECIALHASHTAGS


def get_hashtag() -> str:
    ht = ''
    for item in SPECIALHASHTAGS:
        ht += ' ' + item
    ht += ' ' + random.choice(HASHTAGS)
    return ht


def get_excuse() -> str:
    resp = '🤖'
    resp += random.choice(EXCUSES)
    resp += get_hashtag()

    return resp
