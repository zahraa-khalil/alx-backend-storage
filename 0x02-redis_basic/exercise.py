#!/usr/bin/env python3
"""Redis basic"""


from typing import Union
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
