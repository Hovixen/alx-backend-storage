#!/usr/bin/env python3
""" Writing strings to Redis """
import uuid
import redis
import functools
from typing import Union, Callable


def count_calls(method: Callable) -> Callable:
    """ Decorator function to count the number of times a method is called """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper function """
        key = "{}.{}".format(self.__class__.__qualname__, method.__name__)
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache():
    """ this class contains a store method """
    def __init__(self):
        """ method initializes the class with a private variable """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ method generates a random key, store the input
        data in Redis using the random key and returns the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None):
        """ method takes a key string argument and an optional callable fn
        Retrieves data from Redis based on the key and applies the optional
        callable
        """
        value = self._redis.get(key)
        if value is not None and fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Union[str, bytes]:
        """ method converts Redis value to a string """
        return self.get(key, lambda x: x.decode())

    def get_int(self, key: str) -> int:
        """ method converts Redis value to an integer """
        return self.get(key, lambda x: int(x))
