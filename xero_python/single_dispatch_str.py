# -*- coding: utf-8 -*-
import functools
from types import MappingProxyType


def single_dispatch_str(func=None, key=None):
    """Single-dispatch generic function decorator.

    Transforms a function into a generic function, which can have different
    behaviours depending upon the string value of its first argument.
    The decorated function acts as the default implementation, and additional
    implementations can be registered using the register("key string") attribute
    of the generic function.

    you shall define @single_dispatch_str(key=get_key_function)
    get_key_function has to accept all parameters of the generic function

    """
    if func is None:
        return lambda f: single_dispatch_str(f, key)

    registry = {}

    # get function name for descriptive error messages
    func_name = getattr(func, "__name__", "single_dispatch_str function")

    def default_get_key(*args, **kwargs):
        """default strategy implementation, returns string value of its first argument"""
        if not args:
            raise TypeError(
                "{} requires at least 1 positional argument".format(func_name)
            )

        key = args[0]
        if not isinstance(key, str):
            raise TypeError(
                "{} requires first positional argument to be string type".format(
                    func_name
                )
            )
        return key

    get_key = key or default_get_key

    def dispatch(key):
        """generic_func.dispatch(key) -> <function implementation>

        Runs the dispatch algorithm to return the best available implementation
        for the given string *key* registered on *generic_func*.

        """
        try:
            impl = registry[key]
        except KeyError:
            impl = registry[""]  # default `func` implementation
        return impl

    def register(key, func=None):
        """generic_func.register(key, func) -> func

        Registers a new implementation for the given string *key*
        on a *generic_func*.

        """
        if not isinstance(key, str):
            raise TypeError(
                "{} requires string type key for register".format(func_name)
            )
        if not key:
            raise ValueError(
                "{} requires non empty string type key for register".format(func_name)
            )

        if func is None:
            return lambda f: register(key, f)
        registry[key] = func
        return func

    def wrapper(*args, **kw):
        """wrapper function replacing *generic_func*

        Triggers dispatch function to find registered implementation for
        first argument string value and executes these implementation

        """
        key = get_key(*args, **kw)
        if not isinstance(key, str):
            raise TypeError("{} requires key value to be string type".format(func_name))

        return dispatch(key)(*args, **kw)

    registry[""] = func
    wrapper.register = register
    wrapper.dispatch = dispatch
    wrapper.registry = MappingProxyType(registry)
    functools.update_wrapper(wrapper, func)
    return wrapper
