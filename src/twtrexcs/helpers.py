# coding=utf-8
"""
Add help functions
"""

import random
from twtrexcs.excuses.data import EXCUSES, HASHTAGS, SPECIALHASHTAGS


def get_hashtag() -> str:
    """
    Create string with special and random hashtags
    """

    hash_tags = ""
    for item in SPECIALHASHTAGS:
        hash_tags += " " + item
    hash_tags += " " + random.choice(HASHTAGS)
    return hash_tags


def get_excuse() -> str:
    """
    Create twit for post in Twitter
    """

    resp = "🤖"
    resp += random.choice(EXCUSES)
    resp += get_hashtag()

    return resp
