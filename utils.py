import random
from excuses.data import Excuses


def get_excuse():
    return random.choice(Excuses)
