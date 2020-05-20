# -*- coding: utf-8 -*-
from functools import singledispatch


def getvalue(value, path, default=None):
    """Get a named attribute or item from an object; getvalue(x, 'y.z')
       is equivalent to x.y.z
    When a default argument is given, it is returned when the attribute doesn't
    exist; without it, None returned
    List indexing supported x.0.y.1.z etc.
    """
    paths = path.split(".")
    return get_nested(value, *paths, default=default)


@singledispatch
def get_nested(value, path, *paths, default=None):
    value = getattr(value, path, default)
    if paths:
        return get_nested(value, *paths, default=default)

    return value


@get_nested.register(dict)
def get_nested_dict(value, path, *paths, default=None):
    value = value.get(path, default)
    if paths:
        return get_nested(value, *paths, default=default)

    return value


@get_nested.register(list)
@get_nested.register(tuple)
def get_nested_list(value, path, *paths, default=None):
    try:
        value = value[int(path)]
    except IndexError:
        value = default

    if paths:
        return get_nested(value, *paths, default=default)

    return value
