#!/usr/bin/env python3
""" Writing strings to Redis """
import uuid
import redis
import ast
import functools
from typing import Union, Callable


def count_calls(method: Callable) -> Callable:
    """ Decorator function to count the number of times a method is called """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper function """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Decorator function to store history of inputs and outputs
    for a particular function
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper function """
        input_key = "{}:inputs".format(method.__qualname__)
        output_key = "{}:outputs".format(method.__qualname__)

        self._redis.rpush(input_key, str(args))

        output = method(self, *args, **kwargs)

        self._redis.rpush(output_key, output)
        return output
    return wrapper


def replay(func: Callable):
    """Display the history of calls of a particular function."""
    # Extract class name & method name from the qualified name of the function
    func_name, _ = func.__qualname__.split(':')[:-1]

    # Construct the input and output keys in Redis
    input_key = "{}:inputs".format(func_name)
    output_key = "{}:outputs".format(func_name)

    # Retrieve the input and output lists from Redis
    inputs = [ast.literal_eval(arg.decode())
              for arg in redis_conn.lrange(input_key, 0, -1)]
    outputs = [output.decode() for output in
               redis_conn.lrange(output_key, 0, -1)]

    # Print the history of calls
    print("{} was called {} times:".format(func.__qualname__, len(inputs)))
    for args, output in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(func.__qualname, args, output))


class Cache():
    """ this class contains a store method """
    def __init__(self):
        """ method initializes the class with a private variable """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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
