#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib


def get_log_path(name):
    path = pathlib.Path(__file__).parent / 'logs' / name
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
