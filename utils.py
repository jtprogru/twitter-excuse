import random
from excuses.data import Excuses, Hashtag


def get_hashtag():
    ht = ''
    for item in Hashtag:
        ht += ' ' + item
    return ht


def get_excuse():
    res = random.choice(Excuses)
    res += get_hashtag()
    return res
