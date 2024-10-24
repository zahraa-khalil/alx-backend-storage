#!/usr/bin/env python3
"""Redis basic"""


import string
from typing import Callable, Union
import uuid
import redis


class Cache:
    def __init__(self):
        """Initialize the cache"""
        # Your code here
        self.__redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in the cache"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        """Get data from the cache"""
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        '''Retrieves a string value from a Redis data storage.
        '''
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        '''Retrieves an integer value from a Redis data storage.
        '''
        return self.get(key, lambda x: int(x))
