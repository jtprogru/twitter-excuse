import random
from excuses.data import Excuses, HTag, SpecialHTag


def get_hashtag():
    ht = ''
    for item in SpecialHTag:
        ht += ' ' + item
    ht += ' ' + random.choice(HTag)
#   ht += ' ' + random.choice(HTag)
    return ht


def get_excuse():
    resp = random.choice(Excuses)
    resp += get_hashtag()
    return resp
