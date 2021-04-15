# coding=utf-8


from twtrexcs.helpers import get_excuse, get_hashtag


def test_get_hashtag():
    assert isinstance(get_hashtag(), str)


def test_get_excuse():
    assert isinstance(get_excuse(), str)


def test_length_twitt():
    resp = get_excuse()
    assert len(resp) <= 140

