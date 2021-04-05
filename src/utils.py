# coding=utf-8
import random
from excuses.data import Excuses, HTag, SpecialHTag


def get_hashtag() -> str:
    ht = ''
    for item in SpecialHTag:
        ht += ' ' + item
    ht += ' ' + random.choice(HTag)
    return ht


def get_excuse() -> str:
    resp = '🤖'
    resp += random.choice(Excuses)
    resp += get_hashtag()

    return resp
