#!/usr/bin/env python3
""" Writing strings to Redis """
import uuid
import redis
from typing import Union


class Cache():
    """ this class contains a store method """
    def __init__(self):
        """ method initializes the class with a private variable """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ method generates a random key, store the input
        data in Redis using the random key and returns the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
